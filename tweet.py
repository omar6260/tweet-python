import os
import sys
from tweepy import API
from tweepy import OAuthHandler

''' authentification fonction '''
def gettwitter_auth():
	try:
		consumer_key = os.environ['TWITTER_CONSUMER_KEY']
		consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
		access_token = os.environ['TWITTER_ACCESS_TOKEN']
		access_secret = os.environ['TWITTER_ACCESS_SECRET']
	except KeyError:
		sys.stderr.write("TWITTER_* environment variable not set\n")
		sys.exit(1)
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	return auth

def get_twitter_client():
	auth = twitter_auth()
	client = tweepy.API(auth)	
	return client
if __name__ == '__main__':
	user = input("Enter username: ")
	client = get_twitter_client()
	for status in cursor(client.home_timeline()).items(10):
		print(status.text)