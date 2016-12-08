import time
import random
from scraper import Scraper
from requester import Requester
from converter import Converter
from accountmanager import AccountManager


def main():

	requester = Requester()
	scraper = Scraper()
	converter = Converter() 

	### REQUEST THE GOOGLE NEWS HTML PAGE ###
	url = 'https://news.google.com/'													## the real url to google news
	pickle_file = 'pickledHtml.pkl'
	response = requester.getHtmlBinary(url)
	requester.dumpHtml(response, pickle_file)
	binaryHtml = requester.loadHtml(pickle_file)
	
	### SCRAPE THE HTML PAGE FOR THE NEWS HEADLINES AND URLS ###
	newsList = scraper.scrapeUrls(binaryHtml)
	
	### CONVERT THE SCRAPED HEADLINES INTO SILLY OLDE ENGLISH ###
	

	
	random.seed()
	rand_index = random.randint(0, len(newsList))
	random_pair = newsList[rand_index]
	print('random_pair {}'.format(random_pair))
	print('random_pair[0] {}'.format(random_pair[0]))
	print('random_pair[1] {}'.format(random_pair[1]))
	oldEnglishString = converter.convert(random_pair[0])
	print('oldEnglishString: {}'.format(oldEnglishString))

	status = oldEnglishString + " " + random_pair[1]
	print('status: {}'.format(status))


	### AUTHENTICATE TO THE TWITTER API AND GENERATE A TWEET ###

	acctManager = AccountManager();
	acctManager.getKeys();
	acctManager.authenticate();
	api = acctManager.api;

	api.update_status(status)


if __name__ == '__main__':
	main()


