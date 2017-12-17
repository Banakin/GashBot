# Version 1.1.0 beta  //  Made by Banakin for GashRTs
# https://github.com/Banakin/GashBot

import tweepy
import json

consumer_key = "TwitterAppConsumerKey"
consumer_secret = "TwitterAppConsumerKeySecret"
access_token = "TwitterAppAccessToken"
access_token_secret = "TwitterAppAccessTokenSecret"
handle = "TwitterHandle" # Your twitter bot’s handle WITHOUT the @ sign

print(''' &&&&&&\                      &&\              
&&  __&&\                     && |             
&& /  \__| &&&&&&\   &&&&&&&\ &&&&&&&\         
&& |&&&&\  \____&&\ &&  _____|&&  __&&\        
&& |\_&& | &&&&&&& |\&&&&&&\  && |  && |       
&& |  && |&&  __&& | \____&&\ && |  && |       
\&&&&&&  |\&&&&&&& |&&&&&&&  |&& |  && |       
 \______/  \_______|\_______/ \__|  \__|       
                                               
                                               
                                               
                  &&&&&&&\             &&\     
                  &&  __&&\            && |    
                  && |  && | &&&&&&\ &&&&&&\   
                  &&&&&&&\ |&&  __&&\\_&&  _|  
                  &&  __&&\ && /  && | && |    
                  && |  && |&& |  && | && |&&\ 
                  &&&&&&&  |\&&&&&&  | \&&&&  |
                  \_______/  \______/   \____/ 
                                               
                                               
                                               
Verson 1.1.0 beta // Made by Banakin // https://banakin.net''')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
	global handle
	
	def on_status(self, tweet):
			global handle
			
			# The bots own retweets get found so it attemts to RT the RTs but it dosnt, its ok.
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
						print('[Gash] Not following you, moving on...') # If you see this message twice it means that the bot found its own tweet, its ok.

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['@'+handle])
