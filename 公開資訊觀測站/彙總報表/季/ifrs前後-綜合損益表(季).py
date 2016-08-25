from pandas import *
from sqlite3 import *
from numpy import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\mops.sqlite3')
conn = connect('D:\\mops.sqlite3')
sql = "SELECT * FROM `%s` " % ('ifrs前後-綜合損益表')
inc = read_sql_query(sql, conn).replace('--', nan).replace('', nan)
# inc['年'] = [x.split('/')[0] for x in inc['年季']]
# inc['季'] = [x.split('/')[1] for x in inc['年季']]
# inc['公司代號'] = inc['公司代號'].astype(str).replace('\.0', '', regex=True)
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
inc.dtypes
# def change(s):
#     a = array(s)
#     return Series(append(a[0], a[1:] - a[0:len(s) - 1]),name=s.name)
for i in col1:
    if inc[i].dtypes is dtype('O'):
        inc[[i]] = inc[[i]].astype(float)


def change0(s):
    if s.dtypes == 'object':
        return s
    else:
        return s-s
inc.apply(change0)
inc.groupby(['公司代號', '年']).apply(change0)    # apply applies function to each series of one dataframe(dataframe object)
inc.dtypes
inc[['公司代號']].dtypes=='0'
def change1(df):
    df1 = df[[x for x in list(df) if df[x].dtype != 'object']]
    a1 = array(df1)
    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
    return DataFrame(v, columns=list(df1))
inc0 = inc.groupby(['公司代號', '年']).apply(change1).reset_index(drop=True);inc0
list(inc0)

def change1(df):
    df0 = df[[x for x in list(df) if df[x].dtype == 'object']]
    df1 = df[[x for x in list(df) if df[x].dtype != 'object']]
    a0 = array(df0)
    a1 = array(df1)
    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
    h = hstack((a0, v))
    return DataFrame(h, columns=list(df0) + list(df1))
inc = inc.groupby(['公司代號', '年']).apply(change1).reset_index(drop=True).sort_values(['年', '季', '公司代號']);inc  # apply applies function to each datafrme(group) of one dataframe(groupby object)



table='ifrs前後-綜合損益表(季)'
# ----create table----
names = list(inc)
c = conn.cursor()
sql = "create table `" + table + "`(" + "'" + names[0] + "'"
for n in names[1:len(names)]:
    sql = sql + ',' + "'" + n + "'"
sql = sql + ', PRIMARY KEY (`年`, `季`, `公司代號`))'
c.execute(sql)
# ----inserting data----
sql = 'INSERT INTO `' + table + '` VALUES (?'
n = [',?'] * (len(names) - 1)
for h in n:
    sql = sql + h
sql = sql + ')'
c.executemany(sql, inc.values.tolist())
conn.commit()
print('done')


inc.公司代號=inc.公司代號.astype(str)
sql='insert into `%s`(`%s`) values(%s)'%(table, '`,`'.join(list(inc)), ','.join('?'*len(list(inc))))
c.executemany(sql, inc.values.tolist())
conn.commit()
print('finish')
len(inc['營業收入'])
len(inc['營業收入'][1:] - inc['營業收入'][0:len(inc['營業收入']) - 1])
len(inc['營業收入'][0:len(inc['營業收入']) - 1])
a1=array(inc['營業收入'])
h= hstack((a1[0], a1[1:] - a1[0:len(a1) - 1]))
Series([a1[0], a1[1:] - a1[0:len(a1) - 1]])
a1[0:1].append(a1[0:1])
concat([a1[0], a1[0]])

sf = Series([1, 1, 2, 3, 3, 3])
sf.groupby(sf).filter(lambda x: x.sum() > 0)
sf.filter(lambda x: x.sum() > 0)
tsdf = DataFrame(np.random.randn(1000, 3),
index=date_range('1/1/2000', periods=1000),
columns=['A', 'B', 'C'])
tsdf[::2]
tsdf.ix[::2] = np.nan
grouped = tsdf.groupby(lambda x: x.year)
grouped.fillna(method='pad')