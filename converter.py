from requester import Requester
import requests

class Converter:
	url = "http://api.funtranslations.com/translate/shakespeare.json?text="

	# You%20gave%20Mr.%20Tim%20a%20hearty%20meal%2C%20but%20unfortunately%20what%20he%20ate%20made%20him%20die.


	requester = Requester()

	def convert(self, text):
		request = self.url + self.encodeSpaces(text)
		r = requests.get(request)
		print(r)
	
	def encodeSpaces(self, text):
		text = text.replace(" ", "%20")
		return text


text = "You gave Mr. Tim a hearty meal, but unfortunately what he ate made him die."
converter = Converter()
converter.convert(text)