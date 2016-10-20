import pickle
from bs4 import BeautifulSoup

class Scraper:

	sources = ['cnn', 'usnews', 'cbsnews', 'space', 
			'nytimes', 'espn', 'usatoday', 'independent', 
			'bbc', 'foxnews', 'wsj']
	
	"""Iterate through the html page and find the
	urls that are associated with designated news
	sources.  Essentially eliminates the unwanted
	links to google and other non-news sources.

	Args: 
		content (bytes): the binary html content

	Returns:
		news_urls (str[]): list of strings containing
		any url found in the html page which leads to
		a news story.

	"""
	def scrape(self, content):
		news_urls = []

		soup = BeautifulSoup(content, 'html.parser')
		for link in soup.find_all('a'):
			url_string_attr = link.get('href')
			if url_string_attr:
				if self.isSource(url_string_attr):
				##if 'http' in link.get('href'):
					news_urls.append(url_string_attr)
		return news_urls

	"""Check to see if a url is coming
	from a designated news source.

	Args: 
		url_string (str): the string to search

	Returns:
		(bool) True or False
	"""
	def isSource(self, url_string):
		for source in self.sources:
			if source in url_string:
				return True;
		return False;





