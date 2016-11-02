  # ----import----
from sqlite3 import *
import os
os.chdir('C:\\Users\\ak66h_000\\Documents\\db\\')
# os.chdir('D:/')
conn = connect('mops.sqlite3')
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
id='2316'
com = "'%s'"%(id)
sql = "SELECT * FROM '%s' WHERE 公司代號 LIKE %s" % ('ifrs前後-綜合損益表', com)
inc = read_sql_query(sql, conn).replace('--', 'NaN')
col = ['年', '季', '公司代號', '公司名稱', '營業收入', '營業成本', '營業毛利（毛損）', '未實現銷貨（損）益', '已實現銷貨（損）益', '營業毛利（毛損）淨額', '營業費用',
       '其他收益及費損淨額', '營業利益（損失）', '營業外收入及支出', '稅前淨利（淨損）', '所得稅費用（利益）', '繼續營業單位本期淨利（淨損）', '停業單位損益', '合併前非屬共同控制股權損益',
       '本期淨利（淨損）', '其他綜合損益（淨額）', '合併前非屬共同控制股權綜合損益淨額', '本期綜合損益總額', '淨利（淨損）歸屬於母公司業主', '淨利（淨損）歸屬於共同控制下前手權益',
       '淨利（淨損）歸屬於非控制權益', '綜合損益總額歸屬於母公司業主', '綜合損益總額歸屬於共同控制下前手權益', '綜合損益總額歸屬於非控制權益', '基本每股盈餘（元）', '利息淨收益', '利息以外淨收益',
       '呆帳費用及保證責任準備提存（各項提存）', '淨收益', '保險負債準備淨變動', '支出及費用', '收入', '支出', '會計原則變動累積影響數', '呆帳費用', '會計原則變動之累積影響數', '稀釋每股盈餘',
       '利息收入', '減：利息費用', '收回(提存)各項保險責任準備淨額', '費用', '列計非常損益及會計原則變動累積影響數前損益', '營業支出']
col1 = ['營業收入', '營業成本', '營業毛利（毛損）', '未實現銷貨（損）益', '已實現銷貨（損）益', '營業毛利（毛損）淨額', '營業費用', '其他收益及費損淨額', '營業利益（損失）', '營業外收入及支出',
        '稅前淨利（淨損）', '所得稅費用（利益）', '繼續營業單位本期淨利（淨損）', '停業單位損益', '合併前非屬共同控制股權損益', '本期淨利（淨損）', '其他綜合損益（淨額）',
        '合併前非屬共同控制股權綜合損益淨額', '本期綜合損益總額', '淨利（淨損）歸屬於母公司業主', '淨利（淨損）歸屬於共同控制下前手權益', '淨利（淨損）歸屬於非控制權益', '綜合損益總額歸屬於母公司業主',
        '綜合損益總額歸屬於共同控制下前手權益', '綜合損益總額歸屬於非控制權益', '基本每股盈餘（元）', '利息淨收益', '利息以外淨收益', '呆帳費用及保證責任準備提存（各項提存）', '淨收益',
        '保險負債準備淨變動', '支出及費用', '收入', '支出', '會計原則變動累積影響數', '呆帳費用', '會計原則變動之累積影響數', '稀釋每股盈餘', '利息收入', '減：利息費用',
        '收回(提存)各項保險責任準備淨額', '費用', '列計非常損益及會計原則變動累積影響數前損益', '營業支出']
inc = inc[col]
# def change(s):
#     a = array(s)
#     return Series(append(a[0], a[1:] - a[0:len(s) - 1]),name=s.name)
for i in col1:
    if inc[i].dtypes == 'object':
        inc[[i]] = inc[[i]].astype(float)
inc[['年', '季']]=inc[['年', '季']].astype(str)
def change1(df):
    df0 = df[[x for x in list(df) if df[x].dtype == 'object']]
    df1 = df[[x for x in list(df) if df[x].dtype != 'object']]
    a0 = array(df0)
    a1 = array(df1)
    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
    h = hstack((a0, v))
    return DataFrame(h, columns=list(df0) + list(df1))

inc = inc.groupby(['公司代號', '年']).apply(change1).reset_index(drop=True)  #'季' must be string
inc['grow_s'] = inc['本期綜合損益總額'].pct_change(1)
inc['grow_hy'] = inc['本期綜合損益總額'].rolling(window=2).sum().pct_change(2)
inc[col1] = inc[col1].rolling(window=4).sum()
inc['grow_y'] = inc['本期綜合損益總額'].pct_change(4)
inc['grow'] = inc['本期綜合損益總額'].pct_change(1)
# inc['grow.ma'] = inc['grow'].rolling(window=24).mean()*4
inc['本期綜合損益總額.wma'] = inc.本期綜合損益總額.ewm(com=19).mean() * 4
inc['本期綜合損益總額.ma'] = inc['本期綜合損益總額'].rolling(window=12).mean() * 4
sql = "SELECT * FROM '%s' WHERE 公司代號 LIKE %s"
bal = read_sql_query(sql % ('ifrs前後-資產負債表-一般業', com), conn)
bal[['年', '季']]=bal[['年', '季']].astype(str)
print('mops')

#--- summary ---
conn = connect('summary.sqlite3')
sql = "SELECT * FROM '%s' WHERE 公司代號 LIKE %s" % ('會計師查核報告', com)
ac = read_sql_query(sql, conn).replace('--', 'NaN').rename(columns={'公司代號': '證券代號', '公司簡稱': '證券名稱', '核閱或查核日期': '年月日'}).sort_values(['年', '季', '證券代號']).drop(['簽證會計師事務所名稱', '簽證會計師','簽證會計師.1', '核閱或查核報告類型'], axis=1)
ac[['年', '季']]=ac[['年', '季']].astype(str)
# ac['\u3000 核閱或查核日期'] = ac['\u3000 核閱或查核日期'].replace('-', '/', regex=True)
# ac['\u3000 核閱或查核日期'] = ac['\u3000 核閱或查核日期'].replace('\xa0', '', regex=True)
# com = "'5522%'"
sql = "SELECT * FROM '%s' WHERE 公司代號 LIKE %s"
fin = read_sql_query(sql % ('財務分析', com), conn)
report = mymerge(inc, bal)
report['流動比率'] = report['流動資產'] / report['流動負債']
report['負債佔資產比率'] = report['負債總額'] / report['資產總額']
report['權益報酬率'] = report['綜合損益總額歸屬於母公司業主'] * 2 / (report['權益總額'] + report['權益總額'].shift())
report['profitbility'] = report.綜合損益總額歸屬於母公司業主 / (report.權益總額.shift(4))
report['investment'] = report.權益總額.pct_change(4)
report = report.rename(columns={'公司代號': '證券代號'})
report = mymerge(ac, report)
remcol = ['Unnamed: 21', '待註銷股本股數（單位：股）', 'Unnamed: 22', ]
report = report.drop(remcol, axis=1)
report[['年', '季', '綜合損益總額歸屬於母公司業主', '權益總額', 'profitbility', '權益報酬率']]
list(report)
print('summary')

#--- tse ---
conn = connect('tse.sqlite3')
sql="SELECT * FROM '%s' WHERE 證券代號 LIKE %s"
close = read_sql_query(sql% ('每日收盤行情(全部(不含權證、牛熊證))', com), conn)
value = read_sql_query(sql% ('個股日本益比、殖利率及股價淨值比', com), conn).drop(['證券名稱'], 1)
margin = read_sql_query(sql% ('當日融券賣出與借券賣出成交量值(元)', com), conn)
ins = read_sql_query(sql% ('三大法人買賣超日報(股)', com), conn)
deal = read_sql_query(sql% ('自營商買賣超彙總表 (股)', com), conn).drop(['證券名稱'], 1).fillna(0)
fore = read_sql_query(sql% ('外資及陸資買賣超彙總表 (股)', com), conn).drop(['證券名稱'], 1).rename(columns={'買進股數':'外資買進股數','賣出股數':'外資賣出股數','買賣超股數':'外資買賣超股數','鉅額交易': '外資鉅額交易'}).fillna('no')
trust = read_sql_query(sql% ('投信買賣超彙總表 (股)', com), conn).drop(['證券名稱'], 1).rename(columns={'買進股數':'投信買進股數','賣出股數':'投信賣出股數','買賣超股數':'投信買賣超股數','鉅額交易': '投信鉅額交易'}).fillna('no')
index = read_sql_query("SELECT * FROM '%s' WHERE 指數 LIKE %s"% ('大盤統計資訊', "'建材營造類指數'"), conn).rename(columns={'收盤指數':'建材營造類指數'}).drop(['指數', '漲跌(+/-)'], axis=1).replace('--', nan).replace('---', nan)
rindex = read_sql_query("SELECT * FROM '%s' WHERE 指數 LIKE %s"% ('大盤統計資訊', "'建材營造類報酬指數'"), conn).rename(columns={'收盤指數':'建材營造類報酬指數', '漲跌點數':'r漲跌點數','漲跌百分比(%)':'r漲跌百分比(%)'}).drop(['指數', '漲跌(+/-)'], axis=1).replace('--', nan).replace('---', nan)
fore['外資鉅額交易'] = fore['外資鉅額交易'].replace('*', 'yes').replace(' ', 'no')
trust['投信鉅額交易'] = trust['投信鉅額交易'].replace('*', 'yes').replace(' ', 'no').replace(0, 'no')
close['本益比'] = close['本益比'].replace('0.00', nan) # pe is '0.00' when pe < 0
value['本益比'] = value['本益比'].replace('-', nan)  # pe is '-' when pe < 0
value['股價淨值比'] = value['股價淨值比'].replace('-', nan)
# close['證券代號'] = close['證券代號'].str.strip()
# deal['證券代號'] = deal['證券代號'].str.strip()
# fore['證券代號'] = fore['證券代號'].str.strip()
# trust['證券代號'] = trust['證券代號'].str.strip()
# close['證券名稱'] = close['證券名稱'].str.strip()
sql="SELECT * FROM '%s' WHERE 股票代號 LIKE %s"
xdr = read_sql_query(sql% ('除權息計算結果表', com), conn).rename(columns={'股票代號': '證券代號', '股票名稱': '證券名稱'})
list(close)
list(value)
list(ins)
list(inc)
list(bal)
list(deal)
list(fin)
list(trust)
print('tse')
list(ac)
m=mymerge(close, xdr)
m=mymerge(m, value)
m=mymerge(m, deal)
m[['自營商(自行買賣)賣出股數', '自營商(自行買賣)買賣超股數', '自營商(自行買賣)買進股數', '自營商(避險)賣出股數', '自營商(避險)買賣超股數', '自營商(避險)買進股數', '自營商賣出股數', '自營商買賣超股數', '自營商買進股數']] = m[['自營商(自行買賣)賣出股數', '自營商(自行買賣)買賣超股數', '自營商(自行買賣)買進股數', '自營商(避險)賣出股數', '自營商(避險)買賣超股數', '自營商(避險)買進股數', '自營商賣出股數', '自營商買賣超股數', '自營商買進股數']].fillna(0)
m=mymerge(m, fore)
m=mymerge(m, trust)
m[['投信買進股數', '投信賣出股數', '投信買賣超股數']] = m[['投信買進股數', '投信賣出股數', '投信買賣超股數']].fillna(0)
m[['投信鉅額交易']] = m[['投信鉅額交易']].fillna('no')
m=mymerge(m, index)
m=mymerge(m, rindex)
m=mymerge(m, report)
list(m)
print('merge')
m.dtypes

m.年月日=to_datetime(m.年月日, format='%Y/%m/%d').apply(lambda x: x.date()) # should convert to datetime before sort, or the result is  wrong
m=m.sort_values(['年月日','證券代號']).reset_index(drop=True) # reset_index make the index ascending
m[list(report)] = m[list(report)].apply(fill)
m['淨利（淨損）歸屬於母公司業主'] = m['淨利（淨損）歸屬於母公司業主'].astype(float)
m['綜合損益總額歸屬於母公司業主'] = m['綜合損益總額歸屬於母公司業主'].astype(float)
m['毛利率'] = m['營業毛利（毛損）']/m['營業收入']
m['營業利益率'] = m['營業利益（損失）']/m['營業收入']
m['綜合稅後純益率'] = m['綜合損益總額歸屬於母公司業主']/m['營業收入']
m['time'] = m.index.tolist()
col=['年月日', '證券代號', '證券名稱', '公司名稱', '年', '季']
m = m.replace('--', nan)
m = m[col+[x for x in list(m) if x not in col]]
col=['年月日', '證券代號', '證券名稱', '公司名稱', '年', '季', '漲跌(+/-)', '外資鉅額交易', '投信鉅額交易']
m[[x for x in list(m) if x not in col]] = m[[x for x in list(m) if x not in col]].astype(float)
col=['年月日', '證券代號','time', '成交股數', '成交筆數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '調整收盤價', '漲跌(+/-)', '漲跌價差', '最後揭示買價', '最後揭示買量', '最後揭示賣價',
  '最後揭示賣量', '本益比', '殖利率(%)', '股價淨值比', '自營商(自行買賣)賣出股數', '自營商(自行買賣)買賣超股數', '自營商(自行買賣)買進股數', '自營商(避險)賣出股數', '自營商(避險)買賣超股數',
  '自營商(避險)買進股數', '自營商賣出股數', '自營商買賣超股數', '自營商買進股數', '外資鉅額交易', '外資買進股數', '外資賣出股數', '外資買賣超股數', '投信鉅額交易', '投信買進股數',
  '投信賣出股數', '投信買賣超股數', '基本每股盈餘（元）','每股參考淨值', '流動比率', '負債佔資產比率', '權益報酬率', '毛利率', '營業利益率', '綜合稅後純益率', 'grow_s', 'grow_hy', 'grow_y', 'grow',
    '本期綜合損益總額.wma', '本期綜合損益總額.ma', 'profitbility', 'investment', '建材營造類指數', '漲跌點數', '漲跌百分比(%)', '建材營造類報酬指數', 'r漲跌點數', 'r漲跌百分比(%)']
# m[['profitbility', '權益報酬率']]
print('before dropna')
list(m)
m['a'] = m['權值+息值'].replace(NaN, 0)
m['b'] = m['a'].cumsum()
m['調整收盤價']=m.收盤價+m.b
m = m.drop(['a', 'b'], axis=1)
m=m.dropna(axis=1, how='all')

TWII = web.DataReader("^TWII", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'TWII'})
SSE = web.DataReader("000001.SS", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'SSE'})
HSI = web.DataReader("^HSI", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'HSI'})
# STI = web.DataReader("^STI", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'STI'})
N225 = web.DataReader("^N225", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'N225'})
AXJO = web.DataReader("^AXJO", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'AXJO'})
GSPC = web.DataReader("^GSPC", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'GSPC'})
IXIC = web.DataReader("^IXIC", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'IXIC'})
GDAXI = web.DataReader("^GDAXI", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'GDAXI'})
# FTSE = web.DataReader("^FTSE", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'FTSE'})
STOXX50E = web.DataReader("^STOXX50E", "yahoo").reset_index()[['Date', 'Adj Close']].rename(columns={'Date': '年月日', 'Adj Close':'STOXX50E'})
l = [TWII, SSE, HSI, N225, AXJO, GSPC, IXIC, GDAXI, STOXX50E]
index = reduce(mymerge, l).sort_values(['年月日'])
index.年月日=to_datetime(index.年月日).apply(lambda x: x.date())
print('index')

forr=m[col]
#---- bic ----
conn = connect('bic.sqlite3')
c = conn.cursor()
sql="SELECT * FROM '%s'"
bic = read_sql_query(sql% ('景氣指標及燈號-指標構成項目'), conn)
del bic['年月']
m['年月日']=m['年月日'].astype(str)
m['年'], m['月'] = m['年月日'].str.split('-').str[0].astype(int), m['年月日'].str.split('-').str[1].astype(int)
m.dtypes
m=mymerge(m,bic)
del m['年']
del m['月']
del bic['年']
del bic['月']
m.年月日=to_datetime(m.年月日, format='%Y/%m/%d').apply(lambda x: x.date())

forr=m[col+list(bic)]
forr['lnmo'] = log(forr['調整收盤價']/forr['調整收盤價'].shift(120))
forr['lnr'] = log(forr['調整收盤價']/forr['調整收盤價'].shift())
forr['lnr025'] = log(forr['調整收盤價'].shift(-5)/forr['調整收盤價'])*48
forr['lnr05'] = log(forr['調整收盤價'].shift(-10)/forr['調整收盤價'])*24
forr['lnr1'] = log(forr['調整收盤價'].shift(-20)/forr['調整收盤價'])*12
forr['lnr2'] = log(forr['調整收盤價'].shift(-40)/forr['調整收盤價'])*6
forr['lnr3'] = log(forr['調整收盤價'].shift(-60)/forr['調整收盤價'])*4
forr['lnr6'] = log(forr['調整收盤價'].shift(-120)/forr['調整收盤價'])*2
# forr['lnr025'] = (forr['lnr'].rolling(window=5).mean()*240).shift(-5)
# forr['lnr05'] = (forr['lnr'].rolling(window=10).mean()*240).shift(-10)
# forr['lnr1'] = (forr['lnr'].rolling(window=20).mean()*240).shift(-20)
# forr['lnr2'] = (forr['lnr'].rolling(window=40).mean()*240).shift(-40)
# forr['lnr3'] = (forr['lnr'].rolling(window=60).mean()*240).shift(-60)
# forr['lnr6'] = (forr['lnr'].rolling(window=120).mean()*240).shift(-120)
# forr['r025'] = exp(forr['lnr025'])-1
# forr['r05'] = exp(forr['lnr05'])-1
# forr['r1'] = exp(forr['lnr1'])-1
# forr['r2'] = exp(forr['lnr2'])-1
# forr['r3'] = exp(forr['lnr3'])-1
# forr['r6'] = exp(forr['lnr6'])-1
forr['r025'] = (forr['調整收盤價'].shift(-5)/forr['調整收盤價'])**48-1
forr['r05'] = (forr['調整收盤價'].shift(-10)/forr['調整收盤價'])**24-1
forr['r1'] = (forr['調整收盤價'].shift(-20)/forr['調整收盤價'])**12-1
forr['r2'] = (forr['調整收盤價'].shift(-40)/forr['調整收盤價'])**6-1
forr['r3'] = (forr['調整收盤價'].shift(-60)/forr['調整收盤價'])**4-1
forr['r6'] = (forr['調整收盤價'].shift(-120)/forr['調整收盤價'])**2-1
forr['r025.s']= (forr.r025-forr.r025.mean())/forr.r025.std()
forr['r05.s']= (forr.r05-forr.r05.mean())/forr.r05.std()
forr['r1.s']= (forr.r1-forr.r1.mean())/forr.r1.std()
forr['r2.s']= (forr.r2-forr.r2.mean())/forr.r2.std()
forr['r3.s']= (forr.r3-forr.r3.mean())/forr.r3.std()
forr['r6.s']= (forr.r6-forr.r6.mean())/forr.r6.std()
forr['h_l'] = (forr.最高價-forr.最低價)/forr.調整收盤價
forr['P'] = (forr.最高價+forr.最低價+2*forr.調整收盤價)/4
forr['pch'] = (forr.調整收盤價-forr.調整收盤價.shift())/forr.調整收盤價.shift()
forr['ch'] = forr.調整收盤價.diff()
forr['ch_u'], forr['ch_d'] = forr['ch'], forr['ch']
forr.ix[forr.ch_u < 0, 'ch_u'], forr.ix[forr.ch_d > 0, 'ch_d'] = 0, 0
forr['ch_d'] = forr['ch_d'].abs()
forr['rsi'] = forr.ch_u.ewm(alpha=1/14).mean()/(forr.ch_u.ewm(alpha=1/14).mean()+forr.ch_d.ewm(alpha=1/14).mean())*100 #與r和凱基同,ema的公式與一般的ema不同。公式見http://www.fmlabs.com/reference/default.htm?url=RSI.htm
forr['MA5'] = forr.調整收盤價.rolling(window=5).mean()
forr['MA10'] = forr.調整收盤價.rolling(window=10).mean()
forr['MA20'] = forr.調整收盤價.rolling(window=20).mean()
forr['MA60'] = forr.調整收盤價.rolling(window=60).mean()
forr['MA120'] = forr.調整收盤價.rolling(window=120).mean()
forr['max9'] = forr.最高價.rolling(window=9).max()
forr['min9'] = forr.最低價.rolling(window=9).min()
forr['EMA12'] = forr.P.ewm(alpha=2/13).mean()
forr['EMA26'] = forr.P.ewm(alpha=2/27).mean()
forr['DIF'] = forr['EMA12']-forr['EMA26']
forr['MACD'] = forr.DIF.ewm(alpha=0.2).mean()
forr['MACD1'] = (forr['EMA12']-forr['EMA26'])/forr['EMA26']*100
forr['OSC'] = forr.DIF-forr.MACD
forr['rsv'] = (forr.調整收盤價-forr.min9)/(forr.max9-forr.min9)
forr['k']=forr.rsv.ewm(alpha=1/3).mean()
forr['d']=forr.k.ewm(alpha=1/3).mean()
forr['P1'] = (forr.最高價+forr.最低價+forr.調整收盤價)/3
forr['mavg']=forr.P1.rolling(window=20).mean()
forr['up']=forr.mavg+forr.P1.rolling(window=20).std()
forr['dn']=forr.mavg-forr.P1.rolling(window=20).std()
forr['pctB'] = (forr.P1-forr.dn)/(forr.up-forr.dn)
forr['c_up'] = (forr.調整收盤價-forr.up)/forr.up
forr['c_dn'] = (forr.調整收盤價-forr.dn)/forr.up
forr['std5'] = forr.調整收盤價.rolling(window=5).std()
forr['std10'] = forr.調整收盤價.rolling(window=11).std()
forr['std20'] = forr.調整收盤價.rolling(window=20).std()
forr['sign']=sign(forr['pch'])
forr['trend']=forr['sign']
i=forr[forr['trend']==0].index
while i.tolist() !=[]:
    forr.ix[i, 'trend']=forr.ix[i-1, 'trend'].tolist()
    i = forr[forr['trend'] == 0].index
forr['trend']
i=forr[forr['trend']==1].index
a=array(i)
l=(a[1:]-a[:-1]).tolist()
i=array([ i for i, j in enumerate(l) if j !=1])+1
a[i]
forr['reverse']=forr['trend']*2
forr.ix[a[i], 'reverse']=1

i=forr[forr['trend']==-1].index
a=array(i)
l=(a[1:]-a[:-1]).tolist()
i=array([ i for i, j in enumerate(l) if j !=1])+1
forr.ix[a[i], 'reverse']=-1
forr.ix[(forr['reverse'] ==2) | (forr['reverse'] == -2), 'reverse']=0
i=forr.ix[~isnull(forr['pch']),'pch'].index[0:2]
if forr.ix[i[1], 'pch']>forr.ix[i[1], 'pch'] and forr.ix[i[1], 'pch'] !=0:
    forr.ix[i[1], 'reverse'] = 1
if forr.ix[i[1], 'pch']<forr.ix[i[0], 'pch'] and forr.ix[i[1], 'pch'] !=0:
    forr.ix[i[1], 'reverse'] = -1
forr[['pch', 'trend', 'reverse']].head(100)
del forr['sign']

def f(df, c):
    df['pch_{}'.format(c)] = df[c].pct_change()
    df['sign_{}'.format(c)] = sign(df['pch_{}'.format(c)])
    df['trend_{}'.format(c)] = df['sign_{}'.format(c)]
    i = df[df['trend_{}'.format(c)] == 0].index
    while i.tolist() != []:
        df.ix[i, 'trend_{}'.format(c)] = df.ix[i - 1, 'trend_{}'.format(c)].tolist()
        i = df[df['trend_{}'.format(c)] == 0].index
    df['trend_{}'.format(c)]
    i = df[df['trend_{}'.format(c)] == 1].index
    a = array(i)
    l = (a[1:] - a[:-1]).tolist()
    i = array([i for i, j in enumerate(l) if j != 1]) + 1
    a[i]
    df['reverse_{}'.format(c)] = df['trend_{}'.format(c)] * 2
    df.ix[a[i], 'reverse_{}'.format(c)] = 1

    i = df[df['trend_{}'.format(c)] == -1].index
    a = array(i)
    l = (a[1:] - a[:-1]).tolist()
    i = array([i for i, j in enumerate(l) if j != 1]) + 1
    df.ix[a[i], 'reverse_{}'.format(c)] = -1
    df.ix[(df['reverse_{}'.format(c)] == 2) | (df['reverse_{}'.format(c)] == -2), 'reverse_{}'.format(c)] = 0
    i = df.ix[~isnull(df['pch_{}'.format(c)]), 'pch_{}'.format(c)].index[0:2]
    if df.ix[i[1], 'pch_{}'.format(c)] > df.ix[i[1], 'pch_{}'.format(c)] and df.ix[i[1], 'pch_{}'.format(c)] != 0:
        df.ix[i[1], 'reverse_{}'.format(c)] = 1
    if df.ix[i[1], 'pch_{}'.format(c)] < df.ix[i[0], 'pch_{}'.format(c)] and df.ix[i[1], 'pch_{}'.format(c)] != 0:
        df.ix[i[1], 'reverse_{}'.format(c)] = -1
    del df['sign_{}'.format(c)]
    print(df[['pch_{}'.format(c), 'trend_{}'.format(c), 'reverse_{}'.format(c)]].head(100))

f(forr, 'MA5')
f(forr, 'MA10')
f(forr, 'MA20')
f(forr, 'MA60')
f(forr, 'MA120')

forr['newhl']=forr['reverse']*2
i=forr.ix[forr['reverse'] ==1, 'reverse'].index.tolist()
a=array(i)
l = (forr['調整收盤價'][a] - forr['調整收盤價'][a].shift()).tolist()
i = array([i for i, j in enumerate(l) if j > 0])
forr.ix[a[i], 'newhl'] = 1
i=forr.ix[forr['reverse'] ==-1, 'reverse'].index.tolist()
a=array(i)
l = (forr['調整收盤價'][a] - forr['調整收盤價'][a].shift()).tolist()
i = array([i for i, j in enumerate(l) if j < 0])
forr.ix[a[i], 'newhl'] = -1
forr.ix[(forr['newhl'] == 2) | (forr['newhl'] == -2), 'newhl'] = 0
print(forr[['調整收盤價', 'trend', 'reverse', 'newhl']])

def f(df, c):
    df['newhl_{}'.format(c)] = df['reverse_{}'.format(c)] * 2
    i = df.ix[df['reverse_{}'.format(c)] == 1, 'reverse_{}'.format(c)].index.tolist()
    a = array(i)
    l = (df['{}'.format(c)][a] - df['{}'.format(c)][a].shift()).tolist()
    i = array([i for i, j in enumerate(l) if j > 0])
    df.ix[a[i], 'newhl_{}'.format(c)] = 1
    i = df.ix[df['reverse_{}'.format(c)] == -1, 'reverse_{}'.format(c)].index.tolist()
    a = array(i)
    l = (df['{}'.format(c)][a] - df['{}'.format(c)][a].shift()).tolist()
    i = array([i for i, j in enumerate(l) if j < 0])
    df.ix[a[i], 'newhl_{}'.format(c)] = -1
    df.ix[(df['newhl_{}'.format(c)] == 2) | (df['newhl_{}'.format(c)] == -2), 'newhl_{}'.format(c)] = 0
    print(df[['{}'.format(c), 'trend_{}'.format(c), 'reverse_{}'.format(c), 'newhl_{}'.format(c)]])
f(forr, 'MA5')
f(forr, 'MA10')
f(forr, 'MA20')
f(forr, 'MA60')

forr['d'] = forr.調整收盤價-forr.收盤價
forr['調整開盤價'] = forr.開盤價 + forr.d
forr['調整收盤價'] = forr.收盤價 + forr.ｄ
forr['調整最高價'] = forr.最高價 + forr.d
forr['調整最低價'] = forr.最低價 + forr.ｄ
forr['span'] = abs(forr.調整收盤價-forr.調整開盤價)/forr.調整收盤價
forr['span_hl'] = abs(forr.調整最高價-forr.調整最低價)/forr.調整收盤價
forr['ushadow'] = (forr.調整最高價 - forr[['調整開盤價', '調整收盤價']].max(axis=1))/forr.調整收盤價
forr['lshadow'] = (forr[['調整開盤價', '調整收盤價']].min(axis=1) - forr.調整最低價)/forr.調整收盤價
forr['ushadow/span'] =forr['ushadow']/(forr['span']+0.1**10*forr.調整收盤價)
forr['lshadow/span'] =forr['lshadow']/(forr['span']+0.1**10*forr.調整收盤價)
del forr['d']
forr['h_l_1'] = forr['h_l'].shift()
forr['h_l_2'] = forr['h_l'].shift(2)
forr['ushadow_1'] = forr['ushadow'].shift()
forr['lshadow_1'] = forr['lshadow'].shift()
forr['ushadow/span_1'] = forr['ushadow/span'].shift()
forr['lshadow/span_1'] = forr['lshadow/span'].shift()
forr['spandiff'] = forr.span.diff()
forr['spanldiff'] = forr[['調整開盤價', '調整收盤價']].max(axis=1).diff()

print('forr')

tablename='forr'
forr = mymerge(forr, index).sort_values(['年月日'])
forr['漲跌(+/-)'] = forr['漲跌(+/-)'].replace('＋', 1).replace('－', -1).replace('X', 0).replace(' ', None).astype(float)
forr['外資鉅額交易']=forr['外資鉅額交易'].replace('yes', 1).replace('no', 0).astype(float)
forr['投信鉅額交易']=forr['投信鉅額交易'].replace('yes', 1).replace('no', 0).astype(float)
forr.年月日=forr.年月日.astype(str)
forr.證券代號=forr.證券代號.astype(str)
forr = forr.drop_duplicates(['年月日', '證券代號'])
# list(forr)
conn = connect('mysum.sqlite3')
c = conn.cursor()

sql='ALTER TABLE `%s` RENAME TO `%s0`'%(tablename, tablename)
c.execute(sql)
sql='create table `%s` (`%s`, PRIMARY KEY (%s))'%(tablename, '`,`'.join(list(forr)), '`年月日`, `證券代號`')
c.execute(sql)
sql='insert into `%s`(`%s`) values(%s)'%(tablename, '`,`'.join(list(forr)), ','.join('?'*len(list(forr))))
c.executemany(sql, forr.values.tolist())
conn.commit()
sql="drop table `%s0`"%tablename
c.execute(sql)

# sql = 'DROP TABLE forr'
# c.execute(sql)
# forr.to_sql('forr', conn, index=False)
list(forr)
# forr.to_sql('forr1', connect('C:/Users/ak66h_000/OneDrive/webscrap/djangogirls/mysite/db.sqlite3'))
# forr.to_sql('forr', connect('C:/Users/ak66h_000/OneDrive/testpydev/src/db.sqlite3'), index=False)
# forr.to_csv('C:/Users/ak66h_000/Dropbox/forspark.csv', index=False)
# forr.to_json('C:/Users/ak66h_000/Dropbox/forspark.json',force_ascii=False)
print('finish')

