import praw
import dash
import dash_table
import pandas as pd 
import pprint 
import datetime as dt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.offline as of
import plotly.graph_objs as go

df = pd.read_csv('keywords_unix.csv')



#get the data neg>0
df_neg=df[df["neg"]>0]

#get the data pos>0
df_pos=df[df["pos"]>0]

#20200401
t1=1585695600
#20201001
t2=1601506800
#20210401
t3=1617231600

#total in different time period
time1=df["created"]
number_t1=sum(time11 < t2 for time11 in time1)
print(number_t1)

time2=df["created"]
number_t2=sum(t2 < time22 < t3 for time22 in time2)
print(number_t2)

time3=df["created"]
number_t3=sum(time33 > t3 for time33 in time3)
print(number_t3)

#count the number of neg in different time period
#define time 


print(len(df["neg"]))
print(len(df["pos"]))
#time1

time1neg=df_neg["created"]
numbert1neg=((sum(t1 < time11neg < t2 for time11neg in time1neg)))
print(numbert1neg)

#time2
time2neg=df_neg["created"]
numbert2neg=((sum(t2 < time22neg < t3 for time22neg in time2neg)))
print(numbert2neg)
#time3
time3neg=df_neg["created"]
numbert3neg=((sum(time33neg > t3 for time33neg in time3neg)))
print(numbert3neg)

#count the number of pos in different time period
time1pos=df_pos["created"]
numbert1pos=((sum(t1 < time11pos < t2 for time11pos in time1pos)))


time2pos=df_pos["created"]
numbert2pos=((sum(t2 < time22pos < t3 for time22pos in time2pos)))


time3pos=df_pos["created"]
numbert3pos=((sum(time33pos > t3 for time33pos in time3pos)))


#make list 
negnumber=[numbert1neg,numbert2neg,numbert3neg]
posnumber=[numbert1pos,numbert2pos,numbert3pos]
negrate=[(numbert1neg/number_t1),(numbert2neg/number_t2),(numbert3neg/number_t3)]
posrate=[(numbert1pos/number_t1),(numbert2pos/number_t2),(numbert3pos/number_t3)]

print(negnumber)
print(posnumber)
print(negrate)
print(posrate)
#dashboard
of.offline.init_notebook_mode(connected=True)
neg = go.Scatter(
    x=["2020/4/1-2020/10/1", "2020/10/1-2021/04/01", "2021/04/01-2021/05/30"],
    y= negrate,
    name="negrate"
)
pos = go.Scatter(
    x=["2020/4/1-2020/10/1", "2020/10/1-2021/04/01", "2021/04/01-2021/05/30"],
    y= posrate,
    name="posrate"
)
data = go.Data([neg, pos])
of.plot(data)