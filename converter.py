from requester import Requester
import requests
import json
import demjson

class Converter:
	url = "http://api.funtranslations.com/translate/shakespeare.json?text="

	requester = Requester()

	"""The main function for the converter class.
	Converts a string from normal English to old English.
	Args: 
		texst (str): the string to translate.
	Returns:
		translated string
	"""
	def convert(self, text):
		request = self.url + self.encodeSpaces(text)
		r = requests.get(request, headers={'X-FunTranslations-Api-Secret': self.getTranslateAPIKeys()})
		print(r)
		self.saveJsonToFile(r)
		convertedTweet = self.parseJson()
		return convertedTweet
	
	"""Save Json to a file to help with testing and debugging.
	Args: 
		r (request object): a reference to an HTTP
		request object.
	Returns:
		Nothing
	"""
	def saveJsonToFile(self, r):
		parsed_json = json.loads(r.text)
		with open("translatedJson.json", 'w') as file:
			file.write(str(parsed_json))
	
	"""Parse the JSON returned from the fun translations API.
	Args: 
		None
	Returns:
		translated string
	"""
	def parseJson(self):
		with open("translatedJson.json") as json_file:
			string = json_file.read()
			print('\noriginal string: ' + string)
			#string = self.fixLazyJsonQuotes(string)
			print('\nstring after fixLazy: ' + string)

			try:
				#jsonStuff = json.loads(string)
				jsonStuff = demjson.decode(string)
				print('jsonStuff {}'.format(jsonStuff))
			except Exception as e:
				print('Error trying to load json: {}'.format(e))
				return "ValueError";
			
			try:
				translatedString = jsonStuff["contents"]["translated"]
			except KeyError as ke:
				print(ke)
				return('KeyError')
			translatedString = translatedString.replace("\\", "")
			print('translatedString ' + translatedString)
			return translatedString


	def fixLazyJsonQuotes(self, string):
		# get rid of current escape characters
		string = string.replace("\\\\", "\\")
		# remove any double quotes
		#string = string.replace('"', '')
		# replace single quotes with double quotes
		string = string.replace('\'','\"')
		return string


	def sanitizeString(self, string):
		return string.replace('\\', '')

	def encodeSpaces(self, text):
		text = text.replace(" ", "%20")
		return text

	def getTranslateAPIKeys(self):
		with open("api_key.txt") as keyfile:
			key = keyfile.read()
		return key



if __name__ == '__main__':
	converter = Converter()
	text = "Hello world!"
	converter.parseJson()



		



