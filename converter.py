from requester import Requester
import requests
import json

class Converter:
	url = "http://api.funtranslations.com/translate/shakespeare.json?text="

	requester = Requester()

	def convert(self, text):
		request = self.url + self.encodeSpaces(text)
		r = requests.get(request, headers={'X-FunTranslations-Api-Secret': 'VOM7pNSL2OrpFUhqYyS8igeF'})
		print(r)
		print(r.text)
		print(r.json)
		self.saveJsonToFile(r)
		convertedTweet = self.parseJson()
		return convertedTweet
	
	def saveJsonToFile(self, r):
		parsed_json = json.loads(r.text)
		with open("translatedJson.json", 'w') as file:
			file.write(str(parsed_json))
	
	def parseJson(self):
		with open("translatedJson.json") as json_file:
			string = json_file.read()
			print('\noriginal string: ' + string)
			string = self.fixLazyJsonQuotes(string)
			print('\nstring after fixLazy: ' + string)
			print('\nstring after replacing \" with \\"')
			print(string.replace('"', '\\"'))

			try:
				jsonStuff = json.loads(string.replace('"', '\"'))
			except Error as ve:
				print('Error trying to load json: {}'.format(ve))
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

	"""
	def parseJson(self):
		with open("translatedJson.json") as json_file:
			#string = self.fixLazyJsonQuotes(json_file)
			string = json_file.read()
			print('original string: ' + string)
			startIndex = string.find('translated') + len('translated') + 4
			if string.find('text') < string.find('success')
			stopIndex = string.find('text')-4
			translatedString = string[startIndex:stopIndex]
			print('translated string: ' + translatedString)
			sanitizedString = self.sanitizeString(translatedString)
			print('sanitized string ' + sanitizedString)
			return sanitizedString
	"""
	def sanitizeString(self, string):
		return string.replace('\\', '')

	def encodeSpaces(self, text):
		text = text.replace(" ", "%20")
		return text



if __name__ == '__main__':
	converter = Converter()
	text = "Hello world!"
	converter.convert(text)



		



