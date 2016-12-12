"""
TEST CASES

1.  Got the html page with requests
2.  Parsed out new urls


"""
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
os.sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import unittest
import requests
import pickle
from scraper import Scraper
from requester import Requester
from converter import Converter


class TestScraping(unittest.TestCase):
	requester = Requester()
	scraper = Scraper()
	converter = Converter()
	
	def test_getHtmlBinary(self):
		binary = self.requester.getHtmlBinary('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
		knownBinary = requests.get('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
		self.assertEqual( knownBinary.content, binary )
	
	def test_scrapeHeadlines(self):
		#r = requests.get('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
		r = requests.get('https://news.google.com/')
		newsList = self.scraper.scrapeHeadlines(r.content)
		for news in newsList:
			print(news[1])
		
	def test_sanitizeHeadlines(self):
	    testHeadline = "\'<span class=\"titletext\">This is a headline</span>\'"
	    sanitizedHeadline = self.scraper.sanitizeHeadline(testHeadline)
	    print(sanitizedHeadline)
	    self.assertEqual(sanitizedHeadline, "This is a headline")
	
	def test_encodeSpaces(self):
		text = "All cats enjoy strings"
		encodedText = self.converter.encodeSpaces(text)
		self.assertEqual(encodedText, "All{}cats{}enjoy{}strings".format("%20", "%20", "%20"))

	def test_convert(self):
		text = "You gave Mr. Tim a hearty meal, but unfortunately what he ate made him die."
		convertedText = self.converter.convert(text)
		self.assertEqual(convertedText, "Thou did giveth Mr. Tim a hearty meal,  "
			+ "but unfortunately what he englut did maketh him kicketh the bucket.")


if __name__ == '__main__':
	unittest.main()