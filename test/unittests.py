"""
TEST CASES

1.  Got the html page with requests
2.  Parsed out new urls


"""

import unittest
import requests
import pickle
from scraper import Scraper
from requester import Requester


class TestScraping(unittest.TestCase):
	requester = Requester()
	scraper = Scraper()

	def test_getHtmlBinary(self):
		binary = self.requester.getHtmlBinary('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
		knownBinary = requests.get('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
		self.assertEqual( knownBinary.content, binary )

	
	def test_scrape(self):
		r = requests.get('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
		urls = self.scraper.scrapeUrls(r.content)
		self.assertEqual(urls[0], 'http://www.yahoo.com/')
	


if __name__ == '__main__':
	unittest.main()