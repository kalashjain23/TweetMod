import tweepy
import sight_engine
import config.config as config

def tweeting(tweet):

    auth=tweepy.OAuthHandler(config.consumer_key,config.consumer_secret_key)
    auth.set_access_token(config.access_token,config.access_token_secret)
    api=tweepy.API(auth)

    api.update_status(tweet)