  # ----import----
from sqlite3 import *
import os
os.chdir('C:\\Users\\ak66h_000\\Documents\\db\\')
# os.chdir('D:/')
conn = connect('mysum.sqlite3')
c = conn.cursor()

import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
from functools import *
# from pandas.io import data, wb
# from pandas_datareader import data, wb
# import pandas.io.data as web
import pandas_datareader.data as web

## --- read from sqlite ---
def mymerge(x, y):
    m = merge(x, y, on=[col for col in list(x) if col in list(y)], how='outer')
    return m

# --- report---
def fill(s):
    a = array(0)
    r = s[~isnull(s)].index
    a = append(a, r)
    a = append(a, len(s))
    le = a[1:] - a[:len(a) - 1]
    l = []
    for i in range(len(le)):
        l = l + repeat(s[a[i]], le[i]).tolist()
    return Series(l, name=s.name)


df = read_sql_query("SELECT * FROM '{}'".format('forweb') , conn)
df.OSC
list(df)
sign(df.OSC)
df['OSCsign'] = sign(df.OSC)
df['gr']=0
g=0
for i in range(len(df['OSCsign'])-1):
    try:
        if df['OSCsign'][i]*df['OSCsign'][i+1]<0:
            g+=1
            df['gr'][i+1]=g
        else:
            df['gr'][i+1]=g
    except:
        pass
print(df['gr'])

def minORmax(df):
    if df.max()>0:
        return df.max()
    if df.min()<0:
        return df.min()
    else:
        return df

grouped = df.groupby('gr')
l=grouped['OSC'].apply(minORmax).tolist()

d={}
for i, v in enumerate(l):
    d[i+2]=v
d[0], d[1]=nan, nan
df[['gr1']]=df[['gr']].applymap(lambda x:d[x])

df['change']=0
def OSCbreakpoint(df):
    df=df.reset_index(drop=True)  # without this df.ix[0,'gr1'] is only defined in first group
    if df['OSC'].max()>0:
        for i in range(len(df['gr1'])):
            print(i, len(df['gr1']))
            print(i, df.ix[i,'OSC'], df.ix[i,'gr1'])
            if df.ix[i,'OSC']>df.ix[i,'gr1']:
                print(i, 'yes')
                df.ix[i, 'change'] = 1
                break
        return df
    if df['OSC'].min()<0:
        for i in range(len(df['gr1'])):
            print(i, len(df['gr1']))
            print(i, df.ix[i,'OSC'], df.ix[i,'gr1'])
            if df.ix[i,'OSC']<df.ix[i,'gr1']:
                print(i, 'yes')
                df.ix[i, 'change'] = -1
                break
        return df
    else:
        return df

df1=grouped.apply(OSCbreakpoint).reset_index(drop=True)
print(df1)
df1[['gr','OSC','gr1', 'change']]
df1[df1.change==0]
del df1['OSCsign'];del df1['gr'];del df1['gr1']
