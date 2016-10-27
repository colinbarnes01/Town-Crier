from keys import keys

class AccountManager():

	CONSUMER_KEY = ""
	CONSUMER_KEY_SECRET = ""

	ACCESS_TOKEN = ""
	ACCESS_TOKEN_SECRET = ""

	def __init__(self):
		for key in keys:
			self.CONSUMER_KEY = keys['CONSUMER_KEY']
			self.CONSUMER_KEY_SECRET = keys['CONSUMER_KEY_SECRET']
			self.ACCESS_TOKEN = keys['ACCESS_TOKEN']
			self.ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']
	 
	def getKeys(self):
	    return (self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET, 
	    	self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)

		
