import requests
import pickle

class Requester:

	"""Make a url request.

	Args: 
		url (str): the url to request.
	Returns:
		binary data content of the html page
	"""
	def getHtmlBinary(self, url):
		r = requests.get(url)
		print(r.status_code)
		return r.content

	"""Dumps the html binary to a pickle file

	Args:
		binHtml (bytes):  the binary html content
		filename (str): the file to save the data to

	Returns:
		Nothing
	"""
	def dumpHtml(self, c, filename):
		fd = open(filename, 'wb')
		pickle.dump(c, fd)

	def loadHtml(self, filename):
		fd = open(filename, 'rb')
		return pickle.load(fd)
