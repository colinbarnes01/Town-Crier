import pickle
from bs4 import BeautifulSoup

class Scraper:

	sources = ['cnn', 'usnews', 'cbsnews', 'space', 
			'nytimes', 'espn', 'usatoday', 'independent', 
			'bbc', 'foxnews', 'wsj']
	
	"""Iterate through the html page and print out the
	urls that are associated with designated news
	sources.

	Args: 
		content (bytes): the binary html content

	Returns:
		Nothing

	"""
	def scrape(self, content):
		soup = BeautifulSoup(content, 'html.parser')
		for link in soup.find_all('a'):
			url_string_attr = link.get('href')
			if url_string_attr:
				if self.isSource(url_string_attr):
				##if 'http' in link.get('href'):
					print(url_string_attr)

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





