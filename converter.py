from requester import Requester
import requests
import json
import demjson

class Converter:
	url = "http://api.funtranslations.com/translate/shakespeare.json?text="

	requester = Requester()

	def convert(self, text):
		request = self.url + self.encodeSpaces(text)
		r = requests.get(request, headers={'X-FunTranslations-Api-Secret': 'VOM7pNSL2OrpFUhqYyS8igeF'})
		print(r)
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
			#string = self.fixLazyJsonQuotes(string)
			print('\nstring after fixLazy: ' + string)
			#print('\nstring after replacing \" with \\"')
			#print(string.replace('"', '\\"'))
			#string = string.replace('u', '')
			#print('\nstring without any u\'s: ' + string)
			#string.replace('"', '\"')
			#print('\nstring after replaceing \" with \"')

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



if __name__ == '__main__':
	converter = Converter()
	text = "Hello world!"
	converter.parseJson()



		



