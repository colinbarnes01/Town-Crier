import tweepy
from accountmanager import AccountManager
import unittest



def test_authentication():
	## instatiate a new account manager
	acctManager = AccountManager();
	## get the api credentials from the account manager 
	access_token, access_secret, consumer_key, consumer_secret = acctManager.getKeys()
	
	## send the credentials to twitter.  the authentication won't
	## pass / fail until we actually try to make an api call a couple
	## of lines down 
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	## We will access Twitter exclusively through this newly created api object.
	api = tweepy.API(auth)

	## use the api credentials to do something with the api
	## in this case, print out the contents of the user's
	## timeline to the terminal screen
	try:
		api.home_timeline()
	except tweepy.TweepError as TweepError:
		print('Error: could not authenticate with twitter api')
		print("tweepy error text: {}".format(TweepError.response.text))
		print("twitter api error code: {}".format(TweepError.response) )
	else:
		print('test_authentication passed: twitter api authentication successful')


test_authentication()