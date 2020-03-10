from bs4 import BeautifulSoup
import requests
import csv
import time
import praw
import pandas as pd
import datetime as dt
import re

reddit = praw.Reddit(client_id='mr3bQnCiNhaT2g', \
                     client_secret='psDFyHhoyOtghdOw-XAiO3oMYeI', \
                     user_agent='kopic_bot', \
                     username='R_python96', \
                     password='000011')

subreddit = reddit.subreddit('singapore')
top_subreddit = subreddit.top()
print((top_subreddit))
#for submission in subreddit.top(limit=10):
#    print("Submission title: {},Submission id: {}".format(submission.title, submission.id))

topics_dict = { "title":[],
                "score":[], 
                "id":[], 
                "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[]}

#for every submission, we will append the results into the dictionary that was created
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
print(topics_data)

def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
print(topics_data)

topics_data.to_csv('reddit_singapore.csv', index=False) 