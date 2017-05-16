import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import unicodedata
from os import system
import re
import sys
import json

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        read_tweet(json.loads(data))
        return True

    def on_error(self, status):
        print(status)

auth = tweepy.OAuthHandler('H4INzinwL0wL6W2wzYdg', 'eHv4qQWCvuaO48ZS6MvxIcF3sgh7x0WrRx1LC4kIo')
auth.set_access_token('499462520-fwJVkNqLJwh9E7tIs4tWGq38YumBsm6qki7ldYlr', 'tVyL77sSI5ihry01t4zL1dNjfDKk7wCDGQ2Id6IARak')

# api = tweepy.API(auth)

def say_stream(query = "obama"):
    l = StdOutListener()
    stream = Stream(auth, l)
    stream.filter(track=[query])

def read_tweet(tweet):
    text = unicodedata.normalize('NFKD', tweet["text"]).encode('ascii','ignore')
    print text
    text = re.sub('#', "hashtag ", text) # to replace # with hashtag
    text = re.sub(r"(RT)|@\S+|http\S*", "", text) # Skip these
    text = re.sub(r"([A-Z][a-z]+)(?=[A-Z])", r"\1 ", text) # Turns camel case into separated words
    text = text.lower() #otherwise when people are angry speaker will say every letter out loud
    # print text
    system(espeak \"' + text + '\"')

# if __name__ == "__main__":
#     say_stream(sys.argv[1])
say_stream("alcoholafilm")
