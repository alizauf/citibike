import csv as csv
import pandas as pd
from datetime import datetime
import re

df = pd.read_csv('201508-citibike-tripdata.csv', header=0)

original = datetime.today()
print original
df['month'] = df['starttime'].apply(lambda a: int(re.search('(.)/', a).group(1)))
df['day'] = df['starttime'].apply(lambda a: int(re.search('/(.+)/', a).group(1)))
df['year'] = df['starttime'].apply(lambda a: int(re.search('/(\d{4})\s', a).group(1)))
df['hour'] = df['starttime'].apply(lambda a: int(re.search('\s(\d{2}):',a).group(1)))
df['minute'] = df['starttime'].apply(lambda a: int(re.search(':(\d{2}):',a).group(1)))
df['second'] = df['starttime'].apply(lambda a: int(re.search(':(\d{2})$',a).group(1)))
    #print month.groups(), day.groups(), year.groups(), hour.groups(), minute.groups(), second.groups()


# end = datetime.today()
# print end
# duration = end - original
# print duration
# print df.head()
# print df.tail()


night = df[(df['hour']>18) | (df['hour']<7)]
late_night = df[(df['hour']>21) | (df['hour']<4)]
# # print night.head(100)
# # print night.count()
# print df.describe()
# print night.describe()
# print late_night.describe()

by_hour = df.groupby('hour')['birth year']
print by_hour.head()