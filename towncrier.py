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
			print('SLEEPING FOR 300 SECONDS')
			break
			botContext.changeState()
		else:
			# this while loop exists so that a bot can break out of it
			# and sleep if a rate limiting error is detected
			while(botContext.currentState.status == "READY"):
				

				### REQUEST THE GOOGLE NEWS HTML PAGE ###
				url = 'https://news.google.com/'
				pickle_file = 'pickledHtml.pkl'
				response = requester.getHtmlBinary(url)
				requester.dumpHtml(response, pickle_file)
				binaryHtml = requester.loadHtml(pickle_file)

				### SCRAPE THE HTML PAGE FOR THE NEWS HEADLINES AND URLS ###
				newsList = scraper.scrapeHeadlines(binaryHtml)

				### CONVERT THE SCRAPED HEADLINES INTO OLDE ENGLISH ###	


				# compare old and new string and see if they are the same
				while(True):
					random_pair = getRandomPair(newsList)
					oldEnglishString = converter.convert(random_pair[0])
					if oldEnglishString == 'KeyError':	# this occurs when we have hit the translation rate limit
						botContext.changeState()
						break
					elif oldEnglishString == 'ValueError':	# not sure what this error was by try another headline
						pass
					elif oldEnglishString != random_pair[0]:  # if strings are the same, get another one, else break
						break


					

				#print('oldEnglishString: {}'.format(oldEnglishString))

				tweet = oldEnglishString + " " + random_pair[1]
				print('status: {}'.format(tweet))


				### AUTHENTICATE TO THE TWITTER API AND GENERATE A TWEET ###
				acctManager = AccountManager();
				acctManager.getKeys();
				acctManager.authenticate();
				api = acctManager.api;

				#api.update_status(tweet)
				botContext.changeState()
				break


def getRandomPair(newsList):
	random.seed()
	rand_index = random.randint(0, len(newsList)-1)	#NOTE: randint returns a <= N <= b
	return newsList[rand_index]



if __name__ == '__main__':
	main()



