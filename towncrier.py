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

	url = 'https://news.google.com/'													## the real url to google news
	pickle_file = 'pickledHtml.pkl'

	response = requester.getHtmlBinary(url)
	requester.dumpHtml(response, pickle_file)
	
	binaryHtml = requester.loadHtml(pickle_file)
	
	newsList = scraper.scrapeUrls(binaryHtml)

	print('length of newsList: {}'.format(len(newsList)))
	random.seed()
	rand_index = random.randint(0, len(newsList))
	print('random index: {}'.format(rand_index))
	random_pair = newsList[rand_index]
	print(random_pair)






	### AUTHENTICATE TO THE TWITTER API AND GENERATE A TWEET ###
	"""
	acctManager = AccountManager();
	acctManager.getKeys();
	acctManager.authenticate();
	api = acctManager.api;
	"""

if __name__ == '__main__':
	main()


