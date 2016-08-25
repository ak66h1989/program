# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pandas import *
df = DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
df[['a']]
df[(df.a<0)&(df.b>0)]
df.insert(0,'t', '105年01月01日至105年03月31日')
df[~ df.t.str.contains("季")]
df1=df[~ df.t.str.contains("季")]
df.t.str.extract(r'(\d{3}).+(\d{3})')[0]
df.t.str.findall(r'(\d{3})')
d=dict({'3':1,'6':2, '9':3,'12':4})
df1['年']=df1.t.str.extract(r'(\d{3})').astype(int)+1911
df1['季']=df1.t.str[16].replace(d)

df1.insert(0,'年', df1.t.str.extract(r'(\d{3})').astype(int)+1911)
df1.insert(1,'季', df1.t.str[16].replace(d))
del df1['t']

df[~ df.t.str.contains("季")].年

import sqlite3
df.iloc[0]
date_range('1/1/2000', periods=80)
import os
os.getcwd()

import sqlite3
conn = sqlite3.connect('example.db')

import sqlite3

class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.cursor()
cur.execute("create table test(i)")
cur.execute("insert into test(i) values (1)")
cur.execute("insert into test(i) values (2)")
cur.execute("select mysum(i) from test")
print(cur.fetchone()[0])

from jinja2 import Template
template = Template('Hello {{ name }}!')
template.render(name='John Doe')

import asyncio

async def hello_world():
    print("Hello World!")
    
loop=asyncio.get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(hello_world())


import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()

import time
def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    time.sleep(1)
    return x + y

def print_sum(x, y):
    result = compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))


def f():
    for i in range(5):
        yield i
        print('after', i)
f=f()
next(f)
import json
data = FormData()
data.add_field('file',
               open('report.xls', 'rb'),
               filename='report.xls',
               content_type='application/vnd.ms-excel')
h = hashlib.sha256()


import aiohttp_jinja2
import jinja2
from aiohttp import web

app = web.Application()
aiohttp_jinja2.setup(
    app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))
    
class SiteHandler:
    async def index(self, request):
        return web.Response(text='Hello Aiohttp!')
        
def setup_routes(app, handler, project_root):
    add_route = app.router.add_route
    add_route('GET', '/', handler.index)
    
    
from aiohttp import web

async def hello(request):
    return web.Response(body=b"Hello, world")
    
app = web.Application()
app.router.add_route('GET', '/', hello)
web.run_app(app)

import aiohttp_jinja2
import jinja2

aiohttp_jinja2.setup(
    app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))
    
project_root

app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('/templates/'))

app.router.add_static('/static/',
                      path=str('polls/static'),
                      name='static')
aiohttp_jinja2.get_env(app)


def sort(nb1, nb2):
    if len(nb1) == 0: return nb2
    elif len(nb2) == 0: return nb1
    elif nb1[0] < nb2[0]: return [nb1[0]] + sort(nb1[1:], nb2)
    else: return [nb2[0]] + sort(nb1, nb2[1:])
    
number1 = [4,13,6,6,2,7,2,9,29]
number2 = [4,13,6,6,2,7,2,9,29]
number1.sort()
number2.sort()
sort(number1, number2)

import re
re.search(r'\d{2}', '105年01月01日至105年03月31日')
re.match(r'\d{2}', '105年01月01日至105年03月31日')
re.fullmatch(r'\d{2}', '105年01月01日至105年03月31日')
re.findall(r'\d{2}', '105年01月01日至105年03月31日')[4][1]
'季' in '2016年第2季'
d=dict({'3':1,'6':2, '9':3,'12':4})
for i, j in d:
    print(i,j)
    
list( filter((lambda x: x < 0), range(-5,5)))
[x for x in range(-5,5) if x<0]
hash()
list(map(hash, [x for x in range(-5,5) if x<0]))


list(map(hash, ['0','1','2','3']))
import os
os.system('echo $HOME')
os.system('echo %s' %'$HOME')
os.system('command_1 < input_file | command_2 > output_file')
from numpy import *
df = DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
df = DataFrame({'a' : ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'b' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'c' : np.random.randn(8),
                    'd' : np.random.randn(8)}).sort_values(['a', 'b']).reset_index(drop=True)
a=array(df)
a[0,0]=1
a[:,3]=1
df
df.query('d > 0').assign(e = lambda x: (x['a']/x['b']))
df.apply(mean, axis=1
f = lambda x: x+1
def f(x):
    if x<0: return 'd'
    if x==0: return 'e'
    if x>0: return 'i'
f(2)
        
df.applymap(f)
df['e']=df['d'].map(f)
df.groupby(['A','B'], as_index=False).apply(f)
df.groupby(['A','B'], as_index=False).aggregate(sum)
df.groupby(['A','B'])[['A']].applymap(f)
df=df.sort_values(['a', 'b'])

def change1(df):
    df0 = df[[x for x in list(df) if df[x].dtype == 'O']]
    df1 = df[[x for x in list(df) if df[x].dtype != 'O']]
    a0 = array(df0)
    a1 = array(df1.applymap(f))
#    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
    h = hstack((a0, a1))
    return DataFrame(h, columns=list(df0) + list(df1))

def change1(df):
    df[['f']] = df[['e']].applymap(f)
#    a0 = array(df0)
#    a1 = array(df1)
#    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
#    h = hstack((a0, a1))
    return df
df['e']=df.groupby(['a'])['d'].pct_change()
df = df.groupby(['a']).apply(change1)
#df[['c']].applymap(f)
#df.dtypes

from sqlite3 import *
conn = connect('D:\\tse.sqlite3')
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\tse.sqlite3')
c = conn.cursor()
df = read_sql_query("SELECT * from `每日收盤行情(全部(不含權證、牛熊證))`", conn)
df = read_sql_query("SELECT * from `每日收盤行情(全部(不含權證、牛熊證))` where `證券代號`='2316'", conn)
df
df['e']=df.groupby(['a'])['d'].pct_change()
df['d'][6]=1

def f(x):
    if x=='i' or 'd': return 'd'
    if x==0: return 'e'
    if x>0: return 'i'

def trend(df):
    for i in df['f']:
        if i == 'i' or 'd':

    return df
df.ix[df.f=='i','g']='i'
df.ix[df.f=='d','g']='d'
df['f']=sign(df['e']).astype(str).replace('.0', '')
df['f']=sign(df['e'])
for i in range(len(df)):
    if df['f'][i]=='0.0':
        df['g'][i]=df['f'][i-1]
    else:
        df['g'][i]=df['f'][i]

df['h']=nan
for i in range(1, len(df)):
    if df['g'][i] != df['g'][i-1] and isnull(df['g'][i-1]) !=True:
        df['h'][i]='c'
    else:
        df['h'][i] = 'uc'

sign(df['g'][0])
isnull(df['e'][0])
isnan(df['f'][0])
df['g'][i] != df['g'][i-1] and (isnull(df['g'][2-1]) !=True)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
df[['f']].round(decimals=0)
round(df[['f']], -1)
def rep(s):
    s.replace('.0', '')
'.0'.replace('.0', '')
df[['f']].astype(str).replace('.0', '')
df['f'][1].replace('.0', '')

from pandas import *
from numpy import *
df = read_sql_query("SELECT * from `每日收盤行情(全部(不含權證、牛熊證))` where `證券代號`='2316'", conn)
df['收盤價']=df[['收盤價']].replace('--', NaN).astype(float)
df['change']=df.groupby(['證券代號'])['收盤價'].pct_change()
df['sign']=sign(df['change']).astype(str)
df['trend']=df['sign']
for i in range(len(df)):
    if df['trend'][i]=='0.0':
        df['trend'][i]=df['trend'][i-1]

df['reverse']=nan
for i in range(1, len(df)):
    if df['trend'][i] != df['trend'][i-1] and isnull(df['trend'][i-1]) !=True:
        df['reverse'][i]='r'
    else:
        df['reverse'][i] = 't'
df
from sqlite3 import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\TEJ.sqlite3')
conn1 = connect('D:\\mysum.sqlite3')
c = conn.cursor()
c1 = conn1.cursor()
forr = read_sql_query("SELECT * from `forr`", conn1)
df.to_sql('forr', conn1, index=False)
df = read_sql_query("SELECT * from `xlwings`", conn)
df.to_sql('xlwings', conn1, index=False)

df[['sign', 'trend']]

def mymerge(x, y):
    m = merge(x, y, on=[i for i in list(x) if i in list(y)], how='outer')
    return m

df = mymerge(df, forr)
list(df)

df[['pctB']].apply(lambda x: x - x.shift())
df['收盤價'].map(lambda x: x - x.shift())
df['收盤價'].shift()

def f(x):
    if x=='0.0':
        x=x.shift(1)
        return x
df[['trend']]

def f(x):
    if x != x.shift(1) and isnull(x.shift(1)) !=True:
        x = 'r'
df.max()
df['收盤價'].dtypes=='float64'
list(df['收盤價'])
Series(df)
def f(x):
    x+1
    return x+1
    
f(2)
df.apply(sum)
