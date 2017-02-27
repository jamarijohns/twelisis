twelisis
--------

INSTALLATION-

Easiest way-
pip install twelisis

Pre-requisite->
You have to create a twitter account and also create a twitter app
and store all the authorization details in a separate text file.
Help link-http://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html#auth-tutorial


AIM-
This package aims at the abstraction of extaction of tweets from twitter(using tweepy) so as to focus more on the analysis part.
Analysis part(work under progress) 

You can directly use this,simply do:
(Its better to save passwords in a different file.)

>>>import twelisis as t

>>>t.extract_tweets_for_tag(tag_name,password_file_name)

>>>t.extract_sentiment(output_file_name)


