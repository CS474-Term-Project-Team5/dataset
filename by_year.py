import json
import pandas as pd


df = pd.DataFrame()


for i in range(8):
    with open('koreaherald_1517_{}.json'.format(i), 'r') as f:
        dump_list = json.load(f)
        df = pd.concat([df, pd.DataFrame.from_dict(dump_list)])

df.columns = ['title', 'author', 'time', 'description', 'body', 'section']
df['year'] = pd.DatetimeIndex(df.time).year
df['month'] = pd.DatetimeIndex(df.time).month

for year in [2015, 2016, 2017]:
    d = df[df.year == year][:]
    d.to_csv('koreaherald_{}.csv'.format(year))
