import praw
import dash
import dash_table
import pandas as pd 
import pprint 
import datetime as dt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.offline as of
import plotly.graph_objs as go

#API key
reddit = praw.Reddit(client_id= "********",client_secret= "******",user_agent= "******")



from datetime import datetime

#14subreddits
subreddit = reddit.subreddit('CoronavirusUK+Coronavirus+unitedkingdom+AskUK+CoronavirusMemes+CoronavirusRecession+COVID19+LockdownSkepticism +CoronavirusUKCasual+Coronavirus_help_UK+COVID19_support+COVID19positive+StayingAtHome+CovidAnxiety')

top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=10000)
for submission in subreddit.top(limit=10000):
    print(submission.title, submission.id)
topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
   
topics_data = pd.DataFrame(topics_dict)



df=topics_data
df.to_csv('unixtime.csv', index=False)