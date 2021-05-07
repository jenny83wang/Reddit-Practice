import pandas as pd 
df = pd.read_csv('scoreall_unix.csv')




df["title"]=df["title"].str.lower()

df1=df[df['title'].str.contains("lockdown|covid|covid-19")]
df2=df1[df1['title'].str.contains("stress|anxiety|sad|unhappy")]

'''
df3=df2[df2['title'].str.contains("uk")]
'''
#define time 
#20200401
t1=1585695600
#20201001
t2=1601506800
#20210401
t3=1617231600

#total in different time period
time1=df2["created"]
number_t1=sum(time11 < t2 for time11 in time1)
print(number_t1)

time2=df2["created"]
number_t2=sum(t2 < time22 < t3 for time22 in time2)
print(number_t2)

time3=df2["created"]
number_t3=sum(time33 > t3 for time33 in time3)
print(number_t3)

#df2 group 
df2_t1_neg=[df2["neg"]]
df2_t1_neg=[i for i in df2_t1_neg if i !=0]
print (df2_t1_neg)

'''
#get the data neg>0
df_neg=[df2["neg"]>0]
print(len(df_neg))
#get the data pos>0
df_pos=[df2["pos"]>0]
print(len(df_pos))

'''
'''
#count the number of neg in different time period


print(len(df_neg))
print(len(df_pos))
#time1

df2.to_csv('keywords_unix.csv', index=False)
'''


