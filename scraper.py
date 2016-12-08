import pickle
from bs4 import BeautifulSoup

class Scraper:

	sources = ['cnn', 'usnews', 'cbsnews', 'space.com', 
			'nytimes', 'espn', 'usatoday', 'independent', 
			'bbc', 'foxnews', 'wsj']
	
	"""Iterate through the html page and find the news
	headlines and corresponding urls.
	Args: 
		content (bytes): the binary html content
	Returns:
		news list[[str,str]: list of headline, url pairs (also in a list)
		found in the webpage.  A list was used instead of a tuple because
		I want to update the headlines in the main program.
	"""
	def scrapeHeadlines(self, content):

		newsList = []

		soup = BeautifulSoup(content, 'html.parser')
		for link in soup.find_all('a'):
			try:
				headline = self.getHeadline(str(link))
				# many headline attributes are 'None' in the soup, need to ignore those
				if headline != 'None':
					url_string = link.get('href')
					if self.isNewsSource(url_string):
						headline = headline.encode('utf-8')
						headline = self.sanitizeHeadline(str(headline))
						newsList.append([headline, url_string])					

			except Exception as e:
				print('Exception tryin to parse headlines')

		return newsList

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
		spanStartTag = "\'<span class=\"titletext\">"
		spanEndTag = "</span>\'"
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
				#print("source {} found in {}\n".format(source, url_string))
				return True;
		return False;




