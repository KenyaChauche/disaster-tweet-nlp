import sys
import os
import pandas as pd

class tweeterTool():
    def __init__(self):
        assert "disaster-tweet-nlp" in os.path.abspath(os.curdir)
        while os.path.abspath(os.curdir).split("\\")[-1] != "disaster-tweet-nlp":
            os.chdir("..")
        print(os.path.abspath(os.curdir))
        self.df = pd.read_csv("kaggle_data/train.csv")
        
    def get_tweet(self, tweet_id):
        self.tweet = self.df.query("id == {}".format(tweet_id))
        
    def get_keywords(self):
        self.keywords = self.df.keyword.unique()
        
    def get_locations(self):
        self.locations = self.df.location.unique()