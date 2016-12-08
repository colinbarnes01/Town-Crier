from requester import Requester
import requests
import json

class Converter:
	url = "http://api.funtranslations.com/translate/shakespeare.json?text="

	# You%20gave%20Mr.%20Tim%20a%20hearty%20meal%2C%20but%20unfortunately%20what%20he%20ate%20made%20him%20die.

	requester = Requester()

	def convert(self, text):
		request = self.url + self.encodeSpaces(text)
		r = requests.get(request)
		self.saveJsonToFile(r)
		convertedTweet = self.parseJson()
		return convertedTweet
	
	def saveJsonToFile(self, r):
		parsed_json = json.loads(r.text)
		with open("translatedJson.json", 'w') as file:
			file.write(str(parsed_json))
	
	def parseJson(self):
		with open("translatedJson.json") as json_file:
			string = self.fixLazyJsonQuotes(json_file)
			jsonStuff = json.loads(string)
			translatedString = jsonStuff["contents"]["translated"]
			return (translatedString)

	def fixLazyJsonQuotes(self, fd):
		string = fd.read()
		return string.replace('\'','\"')

	def encodeSpaces(self, text):
		text = text.replace(" ", "%20")
		return text



		

#if __name__ == '__main__':

	#text = "You gave Mr. Tim a hearty meal, but unfortunately what he ate made him die."
	#converter = Converter()
	#converter.convert(text)
	#converter.parseJson()
	#converter.fixLazyJsonQuotes()
