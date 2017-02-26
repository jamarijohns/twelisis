import json
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class tweet_sentiment:

	def read_json(self,path):
		#reading JSON(format of raw tweets)		
		tweets_data=[]
		file=open(path,"r")
		for i in file:
			try:
				tweet=json.loads(i)
				tweets_data.append(tweet)
			except:
				continue
		return tweets_data

 
	def calc_sentment_scores(self,path):
		tweets=pd.DataFrame()
		tweets_data=self.read_json(path)
		tweets['text'] = [tweet.get('text','') for tweet in tweets_data]
		#Sentiment analysis using vader package from nltk
		analyser=SentimentIntensityAnalyzer()
		tweets["neg"]=[(analyser.polarity_scores(i)['neg']) for i in tweets['text']]
		tweets["neu"]=[(analyser.polarity_scores(i)['neu']) for i in tweets['text']]
		tweets["pos"]=[(analyser.polarity_scores(i)['pos']) for i in tweets['text']]
		tweets["compound"]=[(analyser.polarity_scores(i)['compound']) for i in tweets['text']]
		return tweets
