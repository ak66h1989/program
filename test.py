import re
print (re.search(r'\[dup].*','abcd[dup]56'))
print (re.search(r'\[dup].*','abcd[dup]567'))
print (re.search(r'.*\[duplicate]','\u3000\u3000 瘥???砍?豢平銝蒜duplicate]48'))
print (re.search(r'.*\[duplicate].*','\u3000\u3000 [duplicate]48'))
print (re.search(u'^\[duplicate].*','\u3000\u3000 瘥???砍?豢平銝蒜duplicate]70'))

from pandas import *
l=['a',1,2,3,4,5]
df=DataFrame(l)
df.columns=df.ix[0,:]
df=df.ix[1:len(df),:]

l1=['a',2,3,4,5,6,7]
df1=DataFrame(l1)
df1.columns=df1.ix[0,:]
df1=df1.ix[1:len(df1),:]

df=DataFrame()
print(df1)
df2=concat([df,df1],axis=1)
print(df2)
df=read_csv('C:/Users/ak66h_000/OneDrive/webscrap/du2.csv',encoding='big5')
print(df)


from sqlite3 import *

import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
import re
import datetime

conn = connect('C:\\Users\\ak66h_000\\Documents\\TEJ.sqlite3')
conn1 = connect('C:\\Users\\ak66h_000\\Documents\\tse.sqlite3')
# conn1 = connect('C:\\Users\\ak66h_000\\Documents\\summary.sqlite3')
# conn1 = connect('C:\\Users\\ak66h_000\\Documents\\mops.sqlite3')
c = conn.cursor()
c1 = conn1.cursor()


# for i in ['一般業', '保險業', '未知業', '證券業', '金控業', '銀行業']:
#     tablename='資產負債表-'+i
#     print(tablename)
tablename='個股日成交資訊'
df = read_sql_query('select * from `%s`'%(tablename), conn)
names = list(df)
sql = "create table `" +tablename + "`(" + "'" + names[0] + "'"
for n in names[1:len(names)]:
    sql = sql + ',' + "'" + n + "'"
sql = sql + ',PRIMARY KEY (`證券代號`, `證券名稱`, `日期`))'
c1.execute(sql)

name=[]
l=[]
for i in list(df):
    name.append(i)
    l.append('?')
c1.executemany('INSERT INTO `%s` VALUES (%s)'%(tablename, ','.join(l)), df.values.tolist())
conn1.commit()

c.execute('drop table `%s` '%(tablename))


tablename='綜合損益表-一般業'
df = read_sql_query('SELECT * from `'+tablename+'`', conn)
df.to_sql('綜合損益表-一般業', conn1)

conn = connect('C:\\Users\\ak66h_000\\Documents\\TEJ.sqlite3')
with open('C:\\Users\\ak66h_000\\Documents\\dump.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)


def integers():
    i = 1
    while True:
        yield i
        i = i + 1
i=integers()
next(i)
def squares():
    for i in integers():
        yield i * i
s=squares()
next(s)


from aiohttp import web

async def hello(request):
    return web.Response(body=b"Hello, world")
app = web.Application()
app.router.add_route('GET', '/', hello)
web.run_app(app)

class Handler:

    def __init__(self):
        pass

    def handle_intro(self, request):
        return web.Response(body=b"Hello, world")

    async def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        txt = "Hello, {}".format(name)
        return web.Response(text=txt)

handler = Handler()
app.router.add_route('GET', '/intro', handler.handle_intro)
app.router.add_route('GET', '/greet/{name}', handler.handle_greeting)


tablename='綜合損益表-一般業'
conn = connect('C:\\Users\\ak66h_000\\Documents\\summary.sqlite3')
c = conn.cursor()
df = read_sql_query("SELECT * from `%s`"%tablename, conn)
df.dtypes

df=df.replace('--', nan)
sql='create table `%s0` (`%s`, PRIMARY KEY (%s))'%(tablename, '`,`'.join(list(df)), '`年`, `季`, `公司代號`')
c.execute(sql)
sql='insert into `%s0`(`%s`) values(%s)'%(tablename, '`,`'.join(list(df)), ','.join('?'*len(list(df))))
c.executemany(sql, df.values.tolist())
conn.commit()

df = read_sql_query("SELECT * from `%s0`"%tablename, conn)
df.dtypes
df['其他收益及費損淨額']+df['其他收益及費損淨額']
df['其他收益及費損淨額']=df['其他收益及費損淨額'].astype(float)

from aiohttp import web
import aiohttp_jinja2
import jinja2
app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('C:/Users/ak66h_000/OneDrive/webscrap/polls/aiohttpdemo_polls/templates'))


web.run_app(app)
