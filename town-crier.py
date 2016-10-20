from scraper import Scraper
from requester import Requester

def main():
	requester = Requester()
	scraper = Scraper() 

	response = requester.getHtmlBinary('https://news.google.com/')
	requester.dumpHtml(response, 'pickledHtml.pkl')



if __name__ == '__main__':
	main()


