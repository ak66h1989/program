##----- pe is '0.00' when pe < 0 -----

from sqlite3 import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\bic.sqlite3')
c = conn.cursor()

from functools import *
import re
get_option("display.max_rows")
get_option("display.max_columns")
set_option("display.max_rows", 400)
set_option("display.max_columns", 1000)
set_option('display.expand_frame_repr', False)
set_option('display.unicode.east_asian_width', True)

def mymerge(x, y):
    m = merge(x, y, on=[i for i in list(x) if i in list(y)], how='outer')
    return m

from pandas import *
import os
import xlwings as xw
os.chdir('C:/Users/ak66h_000/OneDrive/Finance/國發會/bic/')
os.listdir()
table = '景氣指標及燈號-綜合指數'
ext = '.xls'
b = xw.Book(table + ext)
s = b.sheets['Sheet1']
if isnull(s.range('B1').value) == False:
    if isnull(s.range('A1').value):
        s.range('A1').value = '年月'
    if isnull(s.range('A2').value):
        s.range('A2').value = '--'
    l = s.range('A1').expand().value
    col = ['年月'] + l[0][1:]
    df = DataFrame(l[2:], columns=col)
df.insert(0, '年', df.年月.str.split('-').str[0])
df.insert(1, '月', df.年月.str.split('-').str[1])
df.年 = df.年.astype(int)
df.月 = df.月.astype(int)

sql = 'create table `{}` (`{}`, PRIMARY KEY ({}))'.format(table, '`,`'.join(list(df)), '`年`, `月`')
c.execute(sql)
sql = 'insert into `{}`(`{}`) values({})'.format(table, '`,`'.join(list(df)), ','.join('?'*len(list(df))))
c.executemany(sql, df.values.tolist())
conn.commit()

table='景氣指標及燈號-指標構成項目'
b = xw.Book(table + ext)
s = b.sheets['Worksheet']
if isnull(s.range('B1').value) == False:
    if isnull(s.range('A1').value):
        s.range('A1').value = '年月'
    if isnull(s.range('A2').value):
        s.range('A2').value = '--'
    l = s.range('A1').expand().value
    col = ['年月'] + l[0][1:]
    df = DataFrame(l[2:], columns=col)
df.insert(0, '年', df.年月.str.split('-').str[0])
df.insert(1, '月', df.年月.str.split('-').str[1])
df.年 = df.年.astype(int)
df.月 = df.月.astype(int)
df = df.replace(',', '', regex=True)
df[[x for x in list(df) if x not in ['年', '月', '年月']]] = df[[x for x in list(df) if x not in ['年', '月', '年月']]].astype(float)

sql = 'create table `{}` (`{}`, PRIMARY KEY ({}))'.format(table, '`,`'.join(list(df)), '`年`, `月`')
c.execute(sql)
sql = 'insert into `{}`(`{}`) values({})'.format(table, '`,`'.join(list(df)), ','.join('?'*len(list(df))))
c.executemany(sql, df.values.tolist())
conn.commit()

b = xw.Book('NMI-細項指數.xls')
L = []
for s in b.sheets:
    if isnull(s.range('B1').value)==False:
        if isnull(s.range('A1').value):
            s.range('A1').value='ym'
        if isnull(s.range('A2').value):
            s.range('A2').value='--'
        l = s.range('A1').expand().value
        col = ['ym']+l[0][1:]
        df = DataFrame(l[2:], columns=['ym']+l[0][1:])
        df['industry'] = str(s).split(']')[1].split('>')[0]
        L.append(df)
df = reduce(mymerge, L)
print(df)

for i in b.sheets:
    print(i.range('A3').expand().value)

b.sheets[0].range('A3').value
isnull(s.range('A1').value) == False
str(b.sheets[0]).split(']')[1].split('>')[0]