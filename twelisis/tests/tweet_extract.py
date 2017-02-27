from __future__ import print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



# writing tweets and related data into file
class StdOutListener(StreamListener):
	global fn
	fn=open("raw_tweets_data.txt","a")
	def on_data(self,data):
		print(data,file=fn)
		return True
	def on_error(self,status):
		print(status,file=fn)


class tweepy_app:
	# authenciating the app and streaming	
	def run_app(self,tag_name,file_name):
		self.tag_name=tag_name
		self.file_name=file_name
		f=open(self.file_name,"r") #extract passwords from a different file-comparitively safer
		a=f.read().splitlines()
		access_token,access_token_secret,consumer_key,consumer_secret=a
		f.close()
		l=StdOutListener()
		auth =OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream=Stream(auth,l,language='en',filter_level="medium")
		stream.filter(track=[tag_name])#filtering tweets based on topic
		
	




'''



'''

