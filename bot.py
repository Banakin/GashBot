# Version 1.0.0 beta  //  Made by Banakin for GashRTs
# https://github.com/Banakin/GashBot


import tweepy
import json
import time

consumer_key = "TwitterAppConsumerKey"
consumer_secret = "TwitterAppConsumerKeySecret"
access_token = "TwitterAppAccessToken"
access_token_secret = "TwitterAppAccessTokenSecret"
handle = "TwitterHandle" # Your twitter bot’s handle WITHOUT the @ sign

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

while 1 == 1:
	search = api.search("@"+handle, count=15)
	for tweet in search:
		print('[Gash] Found the following tweet: '+str(tweet.id))
		
		for friendship in api.show_friendship(source_id=tweet.user.id, target_screen_name=handle):
			if friendship.screen_name == handle:
				if friendship.followed_by == True:
					try:
						print('[Gash] Retweeting...')
						api.retweet(tweet.id)
						print('[Gash] Retweeted!')
					except:
						print('[Gash] The tweet has been already retweeted, moving on...')
				else:
					print('[Gash] The poster of the tweet does not follow you, moving on...') # If you see this message twice it means that the bot found its own tweet, its ok.
	time.sleep(45)
