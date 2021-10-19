Introduction

Tweet.py est un programme qui consiste à extraire les dix dernier tweet sur une compte twitter.
Tous d'Aabord avant de commencer il faut avoir un compte twitter ensuit se rendre sur www.developer.twitter.com , pour créer un compte devloppeur, apres avoir créés se compte nous allons créés notre application pour pouvoir utilisé l'api de twitter. Une foi c'est fait nous allons commencés par importé les paquet qu'on a besoin. Dans notre cas nous allons utilisés ces module: tweepy, os sys.

importation des paquet
-------------------------------------------------------------------------------------------------------------------------

import os
import sys
from tweepy import API
from tweepy import OAuthHandler
-------------------------------------------------------------------------------------------------------------------------

'PARTIE AUTHENTIFICATION'
-------------------------------------------------------------------------------------------------------------------------
c'est cette partie qu'on doit définir comment on va utilisé l'Api et les clé qui nous à été fournis par twitter lors de la création de notre application.

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
-------------------------------------------------------------------------------------------------------------------------

Pour finir, ici on vas récupéré les donné que l'utilisateur saisis et aussi limité les nombre de tweet qu'on veut extraire par exemple si c'est 10 ou 12 on utilise se fonction: for status in cursor(client.home_timeline()).items(10):

def get_twitter_client():
	auth = twitter_auth()
	client = tweepy.API(auth)	
	return client
if __name__ == '__main__':
	user = input("Enter username: ")
	client = get_twitter_client()
	for status in cursor(client.home_timeline()).items(10):
		print(status.text)
------------------------------------------------------------------------------------------------------------------------

