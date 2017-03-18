# Twelisis
-- Under Development
### Twelisis is an package that contains some methods that aims at the abstraction and simplification of the process of extraction of tweets from twitter and analysing the sentiments of the extracted tweets.(It makes use of the nltk vader module for sentiment extraction.)


# INSTALLATION steps-

### (1) The easiest way is to do a pip install-
    pip install twelisis
### (2) A tar.gz file is availible in pypi.Unpack it use the functions.
### (3) Else fork the repository and use run it.

# Pre-requisite:

To use the package yow would have to create a twitter account and create and register a twitter app.
Also remember to store all the authorization details in a separate text file.This is
one way to keep you passwords secure.Else you could also use encoding to hide your passwords.


#### Help link-http://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html#auth-tutorial

# You can directly use this,simply do:
(Its better to save passwords in a different file as mentioned before.)-

###### import twelisis as t
###### t.extract_tweets_for_tag(tag_name,password_file_name)
###### t.extract_sentiment(output_file_name)


## This project gives a better idea on how to build a package in python and register it in pypi.
### In fact that was the aim behind building this rather than the functionality itself.
