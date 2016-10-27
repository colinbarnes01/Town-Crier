import pickle
from bs4 import BeautifulSoup

class Scraper:

	sources = ['cnn', 'usnews', 'cbsnews', 'space', 
			'nytimes', 'espn', 'usatoday', 'independent', 
			'bbc', 'foxnews', 'wsj']
	
	"""Iterate through the html page and find the
	urls.

	Args: 
		content (bytes): the binary html content

	Returns:
		urls (str[]): list of urls found in
		the webpage.

	"""
	def scrapeUrls(self, content):
		urls = []

		soup = BeautifulSoup(content, 'html.parser')
		for link in soup.find_all('a'):
			url_string_attr = link.get('href')
			if url_string_attr:
				urls.append(url_string_attr)
		return urls


	"""Iterate through the list of urls and eliminate
	the unwanted links to google and other non-news sources.

	Args: 
		url_list (str[]): list of all urls found in webpage

	Returns:
		news_urls (str[]): list of urls which lead to
		a news story.

	"""
	def getNewsUrls(self, url_ist):
		news_urls = []
		for url in url_list:
			if self.isNewsSource(url):
				news_urls.append(url)
		return news_urls


	"""Check to see if a url is coming
	from a designated news source.

	Args: 
		url_string (str): the string to search

	Returns:
		(bool) True or False
	"""
	def isNewsSource(self, url_string):
		for source in self.sources:
			if source in url_string:
				return True;
		return False;





