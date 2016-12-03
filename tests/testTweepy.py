import tweepy
from accountmanager import AccountManager

def getAPI():
	acctManager = AccountManager()
	acctManager.getKeys()
	acctManager.authenticate()
	api = acctManager.api
	return api

def testAuthentication(api):
	try:
		api.home_timeline()
	except tweepy.TweepError as TweepError:
		print('Error: could not authenticate with twitter api')
		print("tweepy error text: {}".format(TweepError.response.text))
		print("twitter api error code: {}".format(TweepError.response) )
	else:
		print('test_authentication passed: twitter api authentication successful')

def testTweet():
	api.update_status("This is a test")

api = getAPI()
testAuthentication(api)
testTweet()
