
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pandas as pd 


df = pd.read_csv('unixtime.csv')

df1=df['title']
print(df1)
analyzer = SentimentIntensityAnalyzer()


df['neg'] = df['title'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
df['pos'] = df['title'].apply(lambda x:analyzer.polarity_scores(x)['pos'])


df.to_csv('scoreall_unix.csv', index=False)


    

    




'''
def getSentiments(df):
    sid = SentimentIntensityAnalyzer()
    for df1 in df1:
        titles_str = titles_str + " " + titles
    print(sid.polarity_scores(titles_str))
'''