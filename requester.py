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
		code = r.status_code
		print('REQUESTING URL...')
		print( 'requests status code: {}'.format(code) )
		return r.content

	"""Make a url request.

	Args: 
		url (str): the url to request.
	Returns:
		text content of the html page
	"""
	def getHtmlText(self, url):
		r = requests.get(url)
		code = r.status_code
		print( 'requests status code: {}'.format(code) )
		return r.text

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

