from xlwings import *

from sqlite3 import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\mops.sqlite3')
c = conn.cursor()

import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
from functools import *
import re
get_option("display.max_rows")
get_option("display.max_columns")
set_option("display.max_rows", 1000)
set_option("display.max_columns", 1000)
set_option('display.expand_frame_repr', False)
set_option('display.unicode.east_asian_width', True)
def mymerge(x, y):
    m = merge(x, y, on=[i for i in list(x) if i in list(y)], how='outer')
    return m

sql="SELECT * FROM `%s` " % ('ifrs前後-綜合損益表')
inc = read_sql_query(sql, conn).replace('--', nan, regex=True).replace('', nan, regex=True)
# inc['年']=[x.split('/')[0] for x in inc['年季']]
# inc['季']=[x.split('/')[1] for x in inc['年季']]
# inc['公司代號']=inc['公司代號'].astype(str).replace('\.0', '', regex=True)
col=['年', '季', '公司代號', '公司名稱', '營業收入', '營業成本', '營業毛利（毛損）', '未實現銷貨（損）益', '已實現銷貨（損）益', '營業毛利（毛損）淨額', '營業費用', '其他收益及費損淨額', '營業利益（損失）', '營業外收入及支出', '稅前淨利（淨損）', '所得稅費用（利益）', '繼續營業單位本期淨利（淨損）', '停業單位損益', '合併前非屬共同控制股權損益', '本期淨利（淨損）', '其他綜合損益（淨額）', '合併前非屬共同控制股權綜合損益淨額', '本期綜合損益總額', '淨利（淨損）歸屬於母公司業主', '淨利（淨損）歸屬於共同控制下前手權益', '淨利（淨損）歸屬於非控制權益', '綜合損益總額歸屬於母公司業主', '綜合損益總額歸屬於共同控制下前手權益', '綜合損益總額歸屬於非控制權益', '基本每股盈餘（元）', '利息淨收益', '利息以外淨收益', '呆帳費用及保證責任準備提存（各項提存）', '淨收益', '保險負債準備淨變動', '支出及費用', '收入', '支出', '會計原則變動累積影響數', '呆帳費用', '會計原則變動之累積影響數', '稀釋每股盈餘', '利息收入', '減：利息費用', '收回(提存)各項保險責任準備淨額', '費用', '列計非常損益及會計原則變動累積影響數前損益', '營業支出']
col1=['營業收入', '營業成本', '營業毛利（毛損）', '未實現銷貨（損）益', '已實現銷貨（損）益', '營業毛利（毛損）淨額', '營業費用', '其他收益及費損淨額', '營業利益（損失）', '營業外收入及支出', '稅前淨利（淨損）', '所得稅費用（利益）', '繼續營業單位本期淨利（淨損）', '停業單位損益', '合併前非屬共同控制股權損益', '本期淨利（淨損）', '其他綜合損益（淨額）', '合併前非屬共同控制股權綜合損益淨額', '本期綜合損益總額', '淨利（淨損）歸屬於母公司業主', '淨利（淨損）歸屬於共同控制下前手權益', '淨利（淨損）歸屬於非控制權益', '綜合損益總額歸屬於母公司業主', '綜合損益總額歸屬於共同控制下前手權益', '綜合損益總額歸屬於非控制權益', '基本每股盈餘（元）', '利息淨收益', '利息以外淨收益', '呆帳費用及保證責任準備提存（各項提存）', '淨收益', '保險負債準備淨變動', '支出及費用', '收入', '支出', '會計原則變動累積影響數', '呆帳費用', '會計原則變動之累積影響數', '稀釋每股盈餘', '利息收入', '減：利息費用', '收回(提存)各項保險責任準備淨額', '費用', '列計非常損益及會計原則變動累積影響數前損益', '營業支出']
inc=inc[col]
# inc=inc.replace('--', 'NaN')
# inc=inc.replace('-', 'NaN')
# def change(df):
#     a = array(df)
#     return DataFrame(vstack((a[0], a[1:] - a[0:len(df) - 1])), columns=list(df))
inc[col1].dtypes
def change1(df):
    df0 = df[[x for x in list(df) if df[x].dtype == 'O']]
    df1 = df[[x for x in list(df) if df[x].dtype != 'O']]
    a0 = array(df0)
    a1 = array(df1)
    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
    h = hstack((a0, v))
    return DataFrame(h, columns=list(df0)+list(df1))
for i in col1:
    if inc[i].dtypes is dtype('O'):
        try:
            inc[[i]] = inc[[i]].astype(float)
        except Exception as e:
            print(i)
            print(e)
            print(inc[i])
            pass

inc=inc.groupby(['公司代號', '年']).apply(change1).reset_index(drop=True)
inc[col1]=inc[col1].rolling(window=4).sum()
inc['grow'] = inc.groupby(['公司代號'])['本期綜合損益總額'].pct_change(1)
inc['grow.ma'] = inc.groupby(['公司代號'])['grow'].apply(rolling_mean, 24)*4
inc['本期綜合損益總額.wma'] = inc.groupby(['公司代號'])['本期綜合損益總額'].apply(ewma, com=19)*4
inc['本期綜合損益總額.ma'] = inc.groupby('公司代號')['本期綜合損益總額'].apply(rolling_mean, 12)*4
inc['營業收入(百萬元)']=inc['營業收入']/1000
inc=inc[['年',  '季',  '公司代號', '公司名稱', '營業收入(百萬元)', '本期淨利（淨損）', '本期綜合損益總額', '基本每股盈餘（元）', '本期綜合損益總額.wma', '本期綜合損益總額.ma', 'grow', 'grow.ma']]
# inc=inc.sort_values(['公司代號','年季'],ascending=[True,False])
inc = inc.sort_values(['公司代號', '年', '季'])

# df=read_csv('C:/Users/ak66h_000/OneDrive/webscrap/公開資訊觀測站/彙總報表/季/綜合損益表/綜合損益表(季)-dashboard.csv',encoding='cp950')
# df=df[['年季','公司代號','公司名稱','本期淨利（淨損）','本期綜合損益總額','基本每股盈餘（元）','本期綜合損益總額.wma','本期綜合損益總額.ma','grow','grow.ma']]
# df=df.sort_values(['公司代號','年季'],ascending=[True,False])
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\TEJ.sqlite3')
c = conn.cursor()
tse = read_sql_query("SELECT * FROM tse_ch", conn)
tse = tse[['公司代號', '產業別']]
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\summary.sqlite3')
c = conn.cursor()
operation = read_sql_query("SELECT * FROM 營益分析", conn).drop(['營業收入(百萬元)'], axis=1)
# operation['公司代號'] = operation['公司代號'].astype(str).replace('\.0', '', regex=True)
finance = read_sql_query("SELECT * FROM 財務分析", conn)
# finance['公司代號'] = finance['公司代號'].astype(str).replace('\.0', '', regex=True)
# operation['公司代號'].tolist()
# operation['公司名稱'].tolist()
# finance['公司代號'].tolist()
# close['公司代號'].tolist()
# value['公司代號'].tolist()

df = mymerge(inc, operation)
# df['年'] = df['年季'].str.split('/').str[0]
# df['季'] = df['年季'].str.split('/').str[1]
df = mymerge(df, finance)
# df = df.sort_values(['公司代號', '年季'])
df = df.sort_values(['公司代號', '年', '季'])
df = df.groupby('公司代號').last().reset_index()
df = df.drop(['年', '季', '公司簡稱'], 1)

conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\tse.sqlite3')
c = conn.cursor()
close = read_sql_query("SELECT 證券代號, 年月日, 收盤價 FROM `每日收盤行情(全部(不含權證、牛熊證))`", conn)
close = close.rename(columns={'證券代號': '公司代號'})
# close['本益比'] = close['本益比'].replace('0.00', 'NaN')  # pe is '0.00' when pe < 0
# close['公司代號'] = close['公司代號'].str.strip()
close = close.sort_values(['公司代號', '年月日'])
close = close.groupby('公司代號').last().reset_index()
value = read_sql_query("SELECT * FROM 個股日本益比、殖利率及股價淨值比", conn)
value = value.rename(columns={'證券代號': '公司代號'})
value['本益比'] = value['本益比'].replace('-', 'NaN')  # pe is '-' when pe < 0
value['股價淨值比'] = value['股價淨值比'].replace('-', 'NaN')
value = value.groupby('公司代號').last().reset_index() #last when ascending, first when descending
value = value.drop(['年月日', '證券名稱'], 1)
# df.to_csv('C:/Users/ak66h_000/OneDrive/R/dashboard/dashboard/報表.csv', index = False)
# value.to_csv('C:/Users/ak66h_000/OneDrive/R/dashboard/dashboard/value.csv', index = False)
# last.to_csv('C:/Users/ak66h_000/OneDrive/R/dashboard/dashboard/每日收盤行情(全部(不含權證、牛熊證)).csv', index = False)
# tse.to_csv('C:/Users/ak66h_000/OneDrive/R/dashboard/dashboard/industry.csv', index = False)
# df.dtypes
# value.dtypes
# close.dtypes
# tse.dtypes
# m.dtypes
m = mymerge(df, value)
m = mymerge(m, close)
m = mymerge(m, tse)
m['流通在外股數'] = m['本期淨利（淨損）']*1000/m['基本每股盈餘（元）']
m = m.replace('--', 'NaN')
m['收盤價'] = m['收盤價'].astype(float)
m['本益比'] = m['本益比'].astype(float)
m['股價淨值比'] = m['股價淨值比'].astype(float)
m['殖利率(%)'] = m['殖利率(%)'].astype(float)
m['市值'] = m['流通在外股數']*m['收盤價']
m['pe.ave'] = m['市值']/m['本期綜合損益總額.wma']/1000
m['ave'] = (m['本益比']+100/m['殖利率(%)']+8*m['股價淨值比'])/3

m = m[['公司代號', '公司名稱', '產業別', '本期淨利（淨損）', '本期綜合損益總額', '基本每股盈餘（元）', '本期綜合損益總額.wma', 'grow', 'grow.ma', 
             '營業收入(百萬元)', '本益比', '殖利率(%)', '股價淨值比', 'ave', 'pe.ave', '權益報酬率(%)', '毛利率(%)', '營業利益率(%)', '稅前純益率(%)', 
             '稅後純益率(%)', '負債佔資產比率(%)', '長期資金佔不動產、廠房及設備比率(%)', 
             '流動比率(%)', '速動比率(%)', '利息保障倍數(%)', '應收款項週轉率(次)', '平均收現日數', '存貨週轉率(次)', '平均售貨日數', '不動產、廠房及設備週轉率(次)', 
             '總資產週轉率(次)', '資產報酬率(%)', '稅前純益佔實收資本比率(%)', '純益率(%)', '每股盈餘(元)', '現金流量比率(%)', '現金流量允當比率(%)', 
             '現金再投資比率(%)', '流通在外股數', '市值', '收盤價', '年月日']]

conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\TEJ.sqlite3')
c = conn.cursor()
# m[(m['本益比'] < 15) & (m['殖利率(%)'] > 5) & (m['股價淨值比'] < 1.5)].sort_values(['ave'])
xlwings = m[(m['營業收入(百萬元)'] > 3000) & (m['本益比'] < 15) & (m['殖利率(%)'] > 5) & (m['股價淨值比'] < 1.5)].sort_values(['ave'])
sql = 'DROP TABLE xlwings'
c.execute(sql)
xlwings.to_sql('xlwings', conn, index = False)
print('done')

# xlwings = read_sql_query("SELECT * from `xlwings`", conn)
# Range('xlwings', (1,1)).options(index=False).value = xlwings

wb = Workbook('C:\\Users\\ak66h_000\\Desktop\\dashboard.xlsm')
Range('new', (1,1)).options(index=False).value = xlwings
print('finish')

# m[m['公司代號']=='2316']

#----IFRS+preIFRS.xlsm---

# inc = read_sql_query("SELECT * from `ifrs前後-綜合損益表(季)`", conn).sort_values(['年', '季', '公司代號'], ascending= [False, False, True])
# inc['年季'] = inc.年+'/' + inc.季
# col=['年季', '年', '季', '公司代號', '公司名稱', '換算匯率', '換算匯率參考依據']
# col1=[x for x in list(inc) if x not in col]
# inc=inc[['公司代號', '公司名稱', '年季']+col1]
# inc.to_excel('C:/Users/ak66h_000/OneDrive/webscrap/公開資訊觀測站/彙總報表/inc.xlsx', sheet_name='Sheet1', index=False)
# print('finish')
#
# bal = read_sql_query("SELECT * from `ifrs前後-資產負債表-一般業`", conn).sort_values(['年', '季', '公司代號'], ascending= [False, False, True])
# bal['年季'] = bal.年+'/' + bal.季
# col=['年季', '年', '季', '公司代號', '公司名稱', 'Unnamed: 21', 'Unnamed: 22']
# col1=[x for x in list(bal) if x not in col]
# bal = bal[['公司代號', '公司名稱', '年季']+col1]
# bal.to_excel('C:/Users/ak66h_000/OneDrive/webscrap/公開資訊觀測站/彙總報表/bal.xlsx', sheet_name='Sheet1', index=False)
# print('finish')

# col = {'繼續營業單位本期純益（純損）': '繼續營業單位本期淨利（淨損）', '繼續營業單位稅前純益（純損）': '稅前淨利（淨損）', '其他綜合損益（稅後淨額）': '其他綜合損益（淨額）',
#        '所得稅（費用）利益': '所得稅費用（利益）', '利息以外淨損益': '利息以外淨收益', '繼續營業單位稅前淨利（淨損）': '稅前淨利（淨損）',
#        '繼續營業單位本期稅後淨利（淨損）': '繼續營業單位本期淨利（淨損）', '本期稅後淨利（淨損）': '本期淨利（淨損）', '其他綜合損益（稅後）': '其他綜合損益（淨額）',
#        '本期綜合損益總額（稅後）': '本期綜合損益總額', '淨利（損）歸屬於母公司業主': '淨利（淨損）歸屬於母公司業主', '淨利（損）歸屬於共同控制下前手權益': '淨利（淨損）歸屬於共同控制下前手權益',
#        '淨利（損）歸屬於非控制權益': '淨利（淨損）歸屬於非控制權益', '繼續營業單位稅前損益': '稅前淨利（淨損）', '呆帳費用及保證責任準備提存': '呆帳費用及保證責任準備提存（各項提存）',
#        '本期其他綜合損益（稅後淨額）': '其他綜合損益（淨額）', '所得稅利益（費用）': '所得稅費用（利益）', '收益': '營業收入', '營業利益': '營業利益（損失）', '營業外損益': '營業外收入及支出',
#        '其他綜合損益': '其他綜合損益（淨額）'}
# inc0 = read_sql_query("SELECT * from `合併損益表`", conn)
# # inc0['公司代號'].tolist()
# # inc0['公司名稱'].tolist()
# inc = read_sql_query("SELECT * from `綜合損益表-一般業`", conn)
# inc1 = read_sql_query("SELECT * from `綜合損益表-保險業`", conn)
# inc1 = inc1.rename(columns=col)
# inc = mymerge(inc, inc1)
# inc1 = read_sql_query("SELECT * from `綜合損益表-銀行業`", conn)
# inc1['所得稅（費用）利益']=inc1['所得稅（費用）利益']*(-1)
# inc1 = inc1.rename(columns=col)
# inc = mymerge(inc, inc1)
# inc1 = read_sql_query("SELECT * from `綜合損益表-金控業`", conn)
# inc1['所得稅（費用）利益']=inc1['所得稅（費用）利益']*(-1)
# inc1 = inc1.rename(columns=col)
# inc = mymerge(inc, inc1)
# inc1 = read_sql_query("SELECT * from `綜合損益表-證券業`", conn)
# inc1['所得稅利益（費用）']=inc1['所得稅利益（費用）']*(-1)
# inc1 = inc1.rename(columns=col)
# inc = mymerge(inc, inc1)
# inc1 = read_sql_query("SELECT * from `綜合損益表-未知業`", conn)
# inc1 = inc1.rename(columns=col)
# inc2 = mymerge(inc, inc1)

# xlwings = inc3
# import os
# path='C:/Users/ak66h_000/OneDrive/webscrap/公開資訊觀測站/彙總報表'
# os.chdir(path)
# os.listdir()
# wb = Workbook('C:/Users/ak66h_000/OneDrive/webscrap/公開資訊觀測站/彙總報表/IFRS+preIFRS.xlsm')
# Range('new', (1,1)).options(index=False).value = xlwings
#
# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# ws['A1'] = inc3
# wb.save("sample.xlsx")


