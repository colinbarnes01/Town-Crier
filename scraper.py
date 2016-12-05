import pickle
from bs4 import BeautifulSoup

class Scraper:

	sources = ['cnn', 'usnews', 'cbsnews', 'space', 
			'nytimes', 'espn', 'usatoday', 'independent', 
			'bbc', 'foxnews', 'wsj']
	
	"""Iterate through the html page and find the urls.
	Args: 
		content (bytes): the binary html content
	Returns:
		urls (str[]): list of urls found in
		the webpage.
	"""
	def scrapeUrls(self, content):
		urls = []
		headlines = []
		thenews = {}

		soup = BeautifulSoup(content, 'html.parser')
		for link in soup.find_all('a'):
			try:
				headline = self.getHeadline(str(link))
				if headline != 'None':
					url_string_attr = link.get('href')
					if url_string_attr:
						thenews[headline.encode('utf-8')] = url_string_attr

			except Exception as e:
				print('Exception tryin to parse headlines')

		print(thenews)
		return urls

	"""Extracts the headline from the larger tag element found by
	beautiful soup in scrapeUrls
	Args:
		link (str): a portion of the html found by scraping for urls
	Retrns:
		a smaller portion of that html containing just the headline
	"""
	def getHeadline(self, link):
		soup = BeautifulSoup(link, 'html.parser')
		headline = soup.find('span', attrs={'class':'titletext'})
		return str(headline)


	"""remove html tags and other unneccesary clutter from the
	string containing the headline.
	Args:
		headline (str)
	Returns:
		a string containing just the headline
	"""
	def sanitizeHeadline(self, headline):
		if headline[0] == 'b':
			headline = headline[1:]
		spanStartTag = "'<span class=\"titletext\">"
		spanEndTag = "</span>'"
		if spanStartTag in headline:
			index = headline.find(spanStartTag)
			headline = headline[index+len(spanStartTag):]
		if spanEndTag in headline:
			index = headline.find(spanEndTag)
			headline = headline[:index]
		return headline


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




