import cnfg
import tweepy
from sk_markov import generate_tweet

tweet_text = generate_tweet()
print tweet_text

config = cnfg.load(".twitter_config_robama")
auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])
api=tweepy.API(auth)

api.update_status(tweet_text)