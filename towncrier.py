import time
import random
from scraper import Scraper
from requester import Requester
from converter import Converter
from accountmanager import AccountManager
from context import Context


def main():

	requester = Requester()
	scraper = Scraper()
	converter = Converter() 

	botContext = Context()

	# this while loop will always run: this automates the bot
	while(True):
		print(botContext.currentState.status)

		if botContext.currentState.status == "WAITING":
			print('SLEEPING FOR 30 MINUTES')
			#break
			time.sleep(1800)
			botContext.changeState()
		else:
			# this while loop exists so that a bot can break out of it
			# and sleep if a rate limiting error is detected
			while(botContext.currentState.status == "READY"):
				

				############ REQUEST THE GOOGLE NEWS HTML PAGE ##########
				url = 'https://news.google.com/'
				pickle_file = 'pickledHtml.pkl'
				response = requester.getHtmlBinary(url)
				requester.dumpHtml(response, pickle_file)
				binaryHtml = requester.loadHtml(pickle_file)

				### SCRAPE THE HTML PAGE FOR THE NEWS HEADLINES AND URLS ###
				newsList = scraper.scrapeHeadlines(binaryHtml)
				print('********* NEWSLIST ********* \n{}'.format(newsList))

				### CONVERT THE SCRAPED HEADLINES INTO OLDE ENGLISH ###	
				# compare old and new string and see if they are the same
				while(True):
					random_pair = getRandomPair(newsList)
					print('random pair[0]: ' + random_pair[0])
					oldEnglishString = converter.convert(random_pair[0])
					if oldEnglishString == 'KeyError':	# this occurs when we have hit the translation rate limit
						break
					elif oldEnglishString == 'ValueError':	# not sure what this error was by try another headline
						pass
						#break
					#elif oldEnglishString != random_pair[0]:  # if strings are the same, get another one, else break
					elif compareStrings(oldEnglishString, random_pair[0]) != True:
						break
					else:
						print('STRING ARE THE SAME')
						#break

				if oldEnglishString == 'KeyError':	# need to break out of second while loop and wait for rate limit
					botContext.changeState()
					break


				oldEnglishString = cryify(oldEnglishString)

				tweet = oldEnglishString + " " + random_pair[1]
				print('status: {}'.format(tweet))


				### AUTHENTICATE TO THE TWITTER API AND GENERATE A TWEET ###
				acctManager = AccountManager();
				acctManager.getKeys();
				acctManager.authenticate();
				api = acctManager.api;

				try:
					api.update_status(tweet)
					print('changing state after successful tweet')
				except Error as e:
					print('Got an error while trying to tweet: {}'.format(e))

				botContext.changeState()

				break


def compareStrings(str1, str2):
	str1 = str1.replace(" ", "")
	str2 = str2.replace(" ", "")
	str1 = str1.replace("\\", "")
	str2 = str2.replace("\\", "")

	if str1 == str2:
		return True
	return False

def getRandomPair(newsList):
	random.seed()
	rand_index = random.randint(0, len(newsList)-1)	#NOTE: randint returns a <= N <= b
	print('rand_index, {}'.format(rand_index))
	return newsList[rand_index]


def cryify(headline):
	intro = ['Hark!', 'Hear Ye, hear ye!', 'Forsooth, ', 'Forsooth, I say!',
				'Hearken!', '\'Rings Bell\'']
	headline = intro[random.randint(0, len(intro)-1)] + ' ' + headline + '!'
	return headline


if __name__ == '__main__':
	main()



