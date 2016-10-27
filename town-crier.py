from scraper import Scraper
from requester import Requester

def main():
	##url = 'https://news.google.com/'													## the real url to google news
	url = 'http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html'	## use this to test
	##url = 'https://users.cs.cf.ac.uk/Dave.Marshall/PERL/node257.html'
	pickle_file = 'pickledHtml.pkl'

	requester = Requester()
	scraper = Scraper() 

	
	response = requester.getHtmlBinary(url)
	requester.dumpHtml(response, pickle_file)
	
	
	binaryHtml = requester.loadHtml(pickle_file)

	urls = scraper.scrapeUrls(binaryHtml)
	for url in urls:
		print(url)



if __name__ == '__main__':
	main()


