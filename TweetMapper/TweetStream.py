import json
import tweepy
import pickle
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
outputFile = "D:\School\GSU\Skums\\tweets\\tweetStream.2018.11.01.json"
dct = ['wickr']

# dictFile = "./metaDictUnambiguousObj.txt"
# with open(dictFile, "rb") as f:
#     dct = pickle.load(f)

consumer_key = 'zxpk8eJfTd0gGBC3lysulS2MI'
consumer_secret = 'B5ycQyucfRoF17KjTjYAsKa3j8hLukJZokJjOIenYKmdcKWl77'
access_token = '1011000293444767744-0mG00x3sJiFtInhd4pYvyhGXafCxrt'
access_secret = 'caQ0PThDCrTBa7U1JcieAN1H3TYAVuOSVYKkWUOLnUCnk'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(outputFile, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=dct)
