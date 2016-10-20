import requests
import pickle
from bs4 import BeautifulSoup

class Scraper:

	sources = ['cnn', 'usnews', 'cbsnews', 'space', 
			'nytimes', 'espn', 'usatoday', 'independent', 
			'bbc', 'foxnews', 'wsj']
	

	def getHtml(self, url):
		r = requests.get(url)
		print(r.status_code)
		c = r.content
		return c

	"""
	Iterate through the html page and print out the
	urls that are associated with reputable new
	sources
	"""
	def scrape(self, content):
		soup = BeautifulSoup(content, 'html.parser')
		for link in soup.find_all('a'):
			url_string_attr = link.get('href')
			if url_string_attr:
				if self.isSource(url_string_attr):
				##if 'http' in link.get('href'):
					print(url_string_attr)

	def isSource(self, url_string):
		for source in self.sources:
			if source in url_string:
				return True;
		return False;

	def dumpHtml(self, c, filename):
		fd = open(filename, 'wb')
		pickle.dump(c, fd)

	def loadHtml(self, filename):
		fd = open(filename, 'rb')
		return pickle.load(fd)



scraper = Scraper()
##html = scraper.getHtml('https://news.google.com/')
##scraper.dumpHtml(html, 'pickledHtml.pkl')

html = scraper.loadHtml('pickledHtml.pkl')
scraper.scrape(html)


