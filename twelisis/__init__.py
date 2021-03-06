from tweet_extract import tweepy_app
from tweet_sentiments import tweet_sentiment 

def extract_tweets_for_tag(tag_name,passwd_file):
	app=tweepy_app()
	app.run_app(tag_name,passwd_file)

def extract_sentiment(path):
	ts=tweet_sentiment()
	df=ts.calc_sentment_scores(path)
	df.to_csv("output.txt", header=True, index=None, sep=',', encoding="utf-8",mode='a')		
