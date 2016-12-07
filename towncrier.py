import time
from scraper import Scraper
from requester import Requester
from context import BotContext
from accountmanager import AccountManager
from waiting import Waiting

def main():

	### REQUEST THE URL PAGE AND SCRAPE IT ###
	context = BotContext()
	print(context.currentState)
	

	##while True:
		if context.currentState.status == "WAITING":
			print('wating in while loop')
			time.sleep(3)
			context.changeState()

		##url = 'https://news.google.com/'													## the real url to google news
		##url = 'http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html'	## use this to test
		url = 'https://users.cs.cf.ac.uk/Dave.Marshall/PERL/node257.html'
		pickle_file = 'pickledHtml.pkl'

		requester = Requester()
		scraper = Scraper() 

		response = requester.getHtmlBinary(url)
		requester.dumpHtml(response, pickle_file)
		
		binaryHtml = requester.loadHtml(pickle_file)

		urls = scraper.scrapeUrls(binaryHtml)
		for url in urls:
			print(url)


		### AUTHENTICATE TO THE TWITTER API AND GENERATE A TWEET ###
		acctManager = AccountManager();
		acctManager.getKeys();
		acctManager.authenticate();
		api = acctManager.api;

		context.changeState()

		print(context.currentState)


if __name__ == '__main__':
	main()


