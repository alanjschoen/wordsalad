import os
import tweepy
import numpy as np

# sentences = []
# while len(sentences) < 2:
#     textfile = os.popen('python markov.py text_samples/obama.txt 200')
#     sentences = textfile.read().strip().split('.')
#     sentences = [s.strip() for s in sentences]
#     sentences =  [s + '.' for s in sentences[1:] if len(s) < 140]
# tweet_text = sentences[np.argmax(map(len, sentences))]

tweet_text = os.popen('python sk_markov.py').read()

print tweet_text



import cnfg
config = cnfg.load("~/.twitter_config_robama")
auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])
api=tweepy.API(auth)


api.update_status(tweet_text)