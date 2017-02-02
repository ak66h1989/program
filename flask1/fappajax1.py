# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 09:43:49 2016

@author: ak66h_000
"""
from flask import Flask, jsonify, render_template, request
from urllib import parse
from pandas import *
from numpy import *
from sqlite3 import *
import os
path = 'C:/Users/ak66h_000/Documents/db/'
os.chdir(path)

import datetime
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

database = 'mops'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
mops = []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    mops.append(tb)

database = 'mysum'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
mysum = []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    mysum.append(tb)

database = 'summary'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
summary = []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    summary.append(tb)

database = 'tse'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
tse = []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    tse.append(tb)

dic = dict()
for i in mops:
    dic[i] = 'mops'
for i in mysum:
    dic[i] = 'mysum'
for i in summary:
    dic[i] = 'summary'
for i in tse:
    dic[i] = 'tse'

def PostParameters(data):
    requestUrl = request.args.get(data)
    print(requestUrl)
    print([parse.unquote(i) for i in requestUrl.split('&')])
    return [parse.unquote(i) for i in requestUrl.split('&')]
# def getPostParameter(PostParameters, par):
#     for i in PostParameters:
#         if par in i:
#             print(i.split('='))
#             return i.split('=')[1]

def getPostParameter(PostParameters, par):
    l = list(filter(lambda x: par in x, PostParameters))
    l = [i.split('=')[1] for i in l]
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        return l

# l=[i.split('=')[1] for i in []]
# len(l)
# def fn(x):
#     return x if x > 5 else None
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = filter(fn, a)
# b
# list(b)
# list(filter(lambda x: x > 5, a))
# g=(item for item in a if fn(item))
# next(g)

d = dict()
@app.route('/', methods=['GET', 'POST'])   # should contain '/' in tail
def index():
    global d
    d['mops'], d['mysum'], d['summary'], d['tse'] = mops, mysum, summary, tse
    d['mops1'], d['mysum1'], d['summary1'], d['tse1'] = mops, mysum, summary, tse
    d['tab'] = '#tabs-1'
    return render_template('testlist.html', d=d)  #d is a dictionary, should appear in template

@app.route('/listfieldajax/', methods=['GET', 'POST'])
def listfieldajax():
    global tab, df, dbtable
    tab ='#tabs-1'
    d['tab'] = tab
    dbtable = getPostParameter(PostParameters('data'), 'dbtable')
    conn = connect('{}.sqlite3'.format(dic[dbtable]))
    df = read_sql_query("SELECT * from `{}`".format(dbtable), conn)
    d['fields'] = list(df)
    return jsonify({'fields': list(df)})

@app.route('/listfield1ajax/', methods=['GET', 'POST'])
def listfield1ajax():
    global tab, df, dbtable1
    tab ='#tabs-5'
    d['tab'] = tab
    dbtable1 = getPostParameter(PostParameters('data'), 'dbtable1')
    conn = connect('{}.sqlite3'.format(dic[dbtable1]))
    df = read_sql_query("SELECT * from `{}`".format(dbtable1), conn)
    d['fields1'] = list(df)
    return jsonify({'fields1': list(df)})

@app.route('/listfield2ajax/', methods=['GET', 'POST'])
def listfield2ajax():
    global tab, df, dbtable2, fields2
    tab ='#tabs-7'
    d['tab'] = tab
    dbtable2 = getPostParameter(PostParameters('data'), 'dbtable2')
    conn = connect('{}.sqlite3'.format(dic[dbtable2]))
    df = read_sql_query("SELECT * from `{}`".format(dbtable2), conn)
    fields2 = list(df)
    d['fields2'] = list(df)
    return jsonify({'fields2': list(df)})

@app.route('/listfield3ajax/', methods=['GET', 'POST'])
def listfield3ajax():
    global tab, df, dbtable3, fields3
    tab ='#tabs-7'
    d['tab'] = tab
    dbtable3 = getPostParameter(PostParameters('data'), 'dbtable3')
    conn = connect('{}.sqlite3'.format(dic[dbtable3]))
    df = read_sql_query("SELECT * from `{}`".format(dbtable3), conn)
    fields3 = list(df)
    d['fields3'] = list(df)
    return jsonify({'fields3': list(df)})

def ymdFirstList(cols):
    if '年月日' in cols:
        cols.remove('年月日')
        cols.insert(0, '年月日')
    else:
        cols.insert(0, '年月日')
    for c in cols:
        print(c)

@app.route('/query/', methods=['POST'])
def query():
    global mll, df, df1
    cols = request.form.getlist('cols')   # list object, empty is allowed
    d['cols'] = cols
    ymdFirstList(cols)
    database = 'mysum'
    conn = connect('{}.sqlite3'.format(database))
    c = conn.cursor()
    table = 'forr'
    df = read_sql_query('select `{}` from `{}`'.format('`,`'.join(cols), table), conn)
    df = df[cols]
    df['年月日'] = to_datetime(df['年月日'])
    df['年月日'] = df['年月日'].apply(unix_time_millis)
    df = df.dropna(subset=['年月日'])
    df1 = df.copy()
    l = array(df1).tolist()
    d['data'] = [['NaN' if isnull(x) else x for x in i] for i in l]
    d['labels'] = list(df1)
    d['y'] = list(df1)[1:]
    d['ymd'] = df1.年月日.tolist()
    list(df1)
    d['tab'] = '#tabs-2'
    return render_template('testlist.html', d=d)

mll, mll1 = {}, {}
mlineIndex = -1
@app.route('/mlineajax/', methods=['GET', 'POST'])
def mlineajax():
    global mlineIndex, mll, mll1, tab, d
    mlineIndex += 1
    pars = PostParameters('data')
    width = getPostParameter(pars, 'width')
    height = getPostParameter(pars, 'height')
    rangeselector = getPostParameter(pars, 'rangeselector')
    cols = getPostParameter(pars, 'cols')
    ymdFirstList(cols)
    conn = connect('{}.sqlite3'.format(dic[dbtable]))
    df = read_sql_query("SELECT `{}` from `{}`".format('`,`'.join(cols), dbtable), conn)
    list(df)
    df.ix[:, 1:] = df.ix[:, 1:].astype(float)
    d['labels'] = list(df)
    d['data'] = array(df).tolist()
    df['年月日'] = to_datetime(df['年月日'])
    df['年月日'] = df['年月日'].apply(unix_time_millis)
    df = df.dropna(subset=['年月日']).dropna(subset=cols[1:])
    df1 = df.copy()
    l = array(df1).tolist()
    data = [['NaN' if isnull(x) else x for x in i] for i in l]   # don't transfer data to string
    labels = list(df1)
    y = list(df1)[1:]
    ymd = df1.年月日.tolist()
    list(df1)
    print('rangeselector:', rangeselector)
    mll['dy'+str(mlineIndex)] = {'cols':cols, 'data':data, 'labels':labels, 'y':y, 'ymd':ymd, 'df1':df1, 'width':width, 'height':height, 'rangeselector':rangeselector}
    mll1['dy'+str(mlineIndex)] = {'cols':cols, 'data':data, 'labels':labels, 'y':y, 'ymd':ymd, 'df1':df1, 'width':width, 'height':height, 'rangeselector':rangeselector}

    d['mll'] = mll1
    tab ='#tabs-2'
    d['tab'] = tab
    d['tableid']='true'
    # return jsonify({'mlineIndex':mlineIndex, 'id': 'dy' + str(mlineIndex), 'data': data, 'labels': labels, 'rangeselector':rangeselector})
    return jsonify({'mlineIndex':mlineIndex, 'id': 'dy' + str(mlineIndex), 'data': data, 'labels': labels, 'width':width, 'height':height, 'rangeselector':rangeselector})

@app.route('/scaleajax/', methods=['GET', 'POST'])
def scaleajax():
    global mll, mll1, tab
    print('/scaleajax........................................../')
    id = request.args.get('name')
    if request.args.get('value') == 'raw':
        mll1[id]['df1'] = mll[id]['df1'].copy()
        li = array(mll1[id]['df1']).tolist()
        mll1[id]['data'] = [['NaN' if isnull(x) else x for x in a] for a in li].copy()
        print("raw........")
        return jsonify({'mlineIndex': int(id.replace('dy', '')), 'id': id, 'data': mll1[id]['data'], 'labels': mll1[id]['labels'], 'rangeselector': mll1[id]['rangeselector']})
    if request.args.get('value') == 'normalize':
        df = mll1[id]['df1'].copy()
        df.ix[:, 1:] = df.ix[:, 1:].apply(lambda x: (x - x.mean()) / x.std()).copy()
        mll1[id]['df1'] = df.copy()
        li = array(mll1[id]['df1']).tolist()
        mll1[id]['data'] = [['NaN' if isnull(x) else x for x in a] for a in li].copy()
        print("normalize........")
        return jsonify({'mlineIndex': int(id.replace('dy', '')), 'id': id, 'data': mll1[id]['data'], 'labels': mll1[id]['labels'], 'rangeselector': mll1[id]['rangeselector']})
    if request.args.get('value') == 'remove':
        del mll1[id]
        del mll[id]
        print("remove........")
        return jsonify({'mlineIndex': int(id.replace('dy', ''))})

i = 0
@app.route('/mpajax/', methods=['GET', 'POST'])
def mpajax():
    global df, df1, i, L, tab
    L = []
    cols1 = getPostParameter(PostParameters('data'), 'cols1')
    cols2 = [x.replace('%', '').replace('(', '').replace(')', '').replace(' ', '').replace('/', '').replace('+', '') for x in cols1]
    print('cols2:',cols2)
    d['cols1'] = cols1
    cols3 = list(zip(cols1, cols2))
    d['cols3'] = cols3
    for col in cols1:
        cols = [col]
        i += 1
        print(i)
        ymdFirstList(cols)

        conn = connect('{}.sqlite3'.format(dic[dbtable1]))
        df = read_sql_query("SELECT `{}` from `{}`".format('`,`'.join(cols), dbtable1), conn)

        df['年月日'] = to_datetime(df['年月日'])
        df['年月日'] = df['年月日'].apply(unix_time_millis)
        df = df.dropna(subset=['年月日'])
        df1 = df
        l = array(df1).tolist()
        data1 = [['NaN' if isnull(x) else x for x in i] for i in l]
        labels1 = list(df1)
        y1 = list(df1)[1:]
        list(df1)
        ymd1 = df1.年月日.tolist()
        title = cols[1]
        print(title)
        L.append([i, cols1, data1, labels1, y1, ymd1, title])
    # d['L'] = [[1,2,3],[4,5,6]]
    d['L1'] = L
    tab = '#tabs-5'
    d['tab'] = tab
    # l=array(df).tolist()
    # d['q'] =[list(df)]+[['NaN' if isnull(x) else x for x in i] for i in l]
    # return render_template('c3.html', d=d)
    return jsonify({'L1':L})

L=[]
@app.route('/plot1ajax/', methods=['GET','POST'])
def plot1ajax():
    global i, L, tab
    print(i)
    # cols = getPostParameter(PostParameters('data'), 'plot1')
    cols = request.args.get('data')
    print(cols)
    cols = cols.replace('=', '')
    cols = [parse.unquote(i) for i in cols.split('&')]
    print('plot1:', cols)
    cols1 = cols
    ymdFirstList(cols)
    database = 'mysum'
    conn = connect('{}.sqlite3'.format(database))
    c = conn.cursor()
    table = 'forr'
    df = read_sql_query('select `{}` from `{}`'.format('`,`'.join(cols), table), conn)
    df = df[cols]
    df['年月日'] = to_datetime(df['年月日'])
    df['年月日'] = df['年月日'].apply(unix_time_millis)
    df = df.dropna(subset=['年月日'])
    df1 = df
    l = array(df1).tolist()
    data1 = [['NaN' if isnull(x) else x for x in i] for i in l]
    labels1 = list(df1)
    y1 = list(df1)[1:]
    # list(df1)
    ymd1 = df1.年月日.tolist()
    title = cols[1]
    # print(title)
    L.append([i, cols1, data1, labels1, y1, ymd1, title])
    # d['L'] = [[1,2,3],[4,5,6]]
    d['L'] = L
    tab = '#tabs-3'
    d['tab'] = tab
    i += 1
    # print(L)
    return jsonify({'L':L})

import datetime
from calendar import monthrange
s_m ={1:3, 2:6, 3:9, 4:12}
def sm(x):
    return(s_m[x])
mllys, mllys1, comp=[], [], []
k=0
@app.route('/ysajax/', methods=['GET','POST'])
def ysajax():
    global mllys, d, k, comp
    k += 1
    pars = PostParameters('data')
    compid = getPostParameter(pars, 'compid')
    cols = getPostParameter(pars, 'cols2')
    print('cols:', cols)
    print('compid:', compid)
    # cols = request.form.getlist('cols2')
    # compid = request.form['compid']
    comp.append([k, cols, dbtable2, fields2])
    conn = connect('{}.sqlite3'.format(dic[dbtable2]))
    if '季' not in fields2:
        for i in ['公司代號', '公司名稱', '公司簡稱', '年', '季']:
            if i in cols:
                cols.remove(i)
        cols.insert(0, '年')
        df = read_sql_query('select `{}` from `{}` where `公司代號`="{}"'.format('`,`'.join(cols), dbtable2, compid), conn)
        df['年月日'] = df['年'].astype(str) + '-12-31'
        df = df.drop(['年'], axis=1)
    else:
        for i in ['公司代號', '公司名稱', '年', '季']:
            if i in cols:
                cols.remove(i)
        cols.insert(0, '年')
        cols.insert(1, '季')
        for c in cols:
            print(c)
        df = read_sql_query('select `{}` from `{}` where `公司代號`="{}"'.format('`,`'.join(cols), dbtable2, compid), conn)
        df['季'] = df['季'].astype(int)
        df['月'] = df.季.apply(sm)
        list(df)
        df['日'] = 1
        df['年月日'] = df['年'].astype(str) + '/' + (df['月']).astype(str) + '/' + df['日'].astype(str)
        df['年月日'] = to_datetime(df['年月日'], format='%Y/%m/%d')
        df['年月日'] = df['年月日'].apply(lambda x: datetime.datetime(x.year, x.month, monthrange(x.year, x.month)[1]))
        df = df.drop(['年', '季', '月', '日'], axis=1)
        df['年月日'] = df['年月日'].astype(str)  # must be string

    df = df[[list(df)[-1]]+list(df)[:-1]]
    df = df.replace('--', 'NaN', regex=True)
    df.ix[:, 1:] = df.ix[:, 1:].astype(float)
    print(df)
    l = array(df).tolist()
    data = [list(df)]+[['NaN' if isnull(x) else x for x in i] for i in l]
    print(data)
    mllys.append([k, data, compid])
    mllys1.append([k, data, compid])
    d['mllys'] = mllys
    return jsonify({'mllys':mllys})

@app.route('/removeajax/', methods=['GET','POST'])
def removeajax():
    global mllys, mllys1, tab, d
    print('removeajax')
    name = getPostParameter(PostParameters('name'), 'name')

    for i, l in enumerate(mllys1):
        print(i, 'c3' + str(l[0]), name, 'c3' + str(l[0]) == name)

    for i, l in enumerate(mllys1):
        if 'c3' + str(l[0]) == name:
            mllys1.pop(i)
            print(mllys1)
            mllys.pop(i)
            comp.pop(i)
            d['mllys'] = mllys1
            tab = '#tabs-7'
            d['tab'] = tab
            return jsonify({'s':'removeajax'})

@app.route('/changeallajax/', methods=['GET','POST'])
def changeallajax():
    global mllys, mllys1, d, k, comp
    mllys, mllys1 =[], []
    compid = getPostParameter(PostParameters('data'), 'compid')
    print('compid:', compid)
    # compid=request.form['compid1']
    for l in comp:
        k, cols, dbtable2, fields2 = l[0], l[1], l[2], l[3]
        conn = connect('{}.sqlite3'.format(dic[dbtable2]))
        if '季' not in fields2:
            for i in ['公司代號', '公司名稱', '公司簡稱', '年', '季']:
                if i in cols:
                    cols.remove(i)
            cols.insert(0, '年')
            df = read_sql_query('select `{}` from `{}` where `公司代號`="{}"'.format('`,`'.join(cols), dbtable2, compid), conn)
            df['年月日'] = df['年'].astype(str) + '-12-31'
            df = df.drop(['年'], axis=1)
        else:
            for i in ['公司代號', '公司名稱', '年', '季']:
                if i in cols:
                    cols.remove(i)
            cols.insert(0, '年')
            cols.insert(1, '季')
            for c in cols:
                print(c)
            df = read_sql_query('select `{}` from `{}` where `公司代號`="{}"'.format('`,`'.join(cols), dbtable2, compid), conn)
            df['月'] = df.季.apply(sm)
            list(df)
            df['日'] = 1
            df['年月日'] = df['年'].astype(str) + '/' + (df['月']).astype(str) + '/' + df['日'].astype(str)
            df['年月日'] = to_datetime(df['年月日'], format='%Y/%m/%d')
            df['年月日'] = df['年月日'].apply(lambda x: datetime.datetime(x.year, x.month, monthrange(x.year, x.month)[1]))
            df = df.drop(['年', '季', '月', '日'], axis=1)
            df['年月日'] = df['年月日'].astype(str)  # must be string

        df = df[[list(df)[-1]]+list(df)[:-1]]
        df = df.replace('--', 'NaN', regex=True)
        df.ix[:,1:] = df.ix[:,1:].astype(float)
        print('df:', df)
        l = array(df).tolist()
        data = [list(df)]+[['NaN' if isnull(x) else x for x in i] for i in l]
        print('data:', data)
        mllys.append([k, data, compid])
        mllys1.append([k, data, compid])
        d['mllys'] = mllys
        print('mllys', mllys)
    return jsonify({'mllys':mllys})

@app.route('/repajax/', methods=['GET', 'POST'])
def repajax():
    global report, tb, d, compid
    report=[]
    tb=[]
    database = 'summary'
    conn = connect('{}.sqlite3'.format(database))
    c = conn.cursor()
    compid = getPostParameter(PostParameters('data'), 'compid_report')
    print(compid)

    # compid='5522'
    # compid = request.form['compid_report']
    d['compid_report'] = compid
    # table = '綜合損益表-一般業'
    # table = '資產負債表-一般業'
    for table in ['綜合損益表-一般業', '資產負債表-一般業']:
        df = read_sql_query('select * from `{}` where `公司代號`="{}"'.format(table, compid), conn)
        d['compname']=df.ix[len(df)-1, '公司名稱']
        color={1:'rgb(0,255,0)', 2:'rgb(0, 190, 255)', 3:'orange', 4:'rgb(255, 75, 140)'}
        df2=df.copy()
        df3=df.copy()
        df3.ix[:, 4:] = df3.ix[:, 4:].replace('--', 0)
        df3.ix[:, 4:] = df3.ix[:, 4:].astype(float)
        for i in color:
            df2.ix[df.季==i, 2:]=color[i]
        smd={1:'3/31', 2:'6/30', 3:'9/30', 4:'12/31'}
        # df['年季'] = df['年'].astype(str) + '年第' + df['季'].astype(str) + '季'
        df['年季'] = df['年'].astype(str)+'/' + df['季'].apply(lambda x: smd[x])
        for i in range(len(df3)):
            for j in range(df3.shape[1]):
                try:
                    if df3.iloc[i, j] < 0:
                        df2.iloc[i, j] = 'red'
                except:
                    pass
        df2['年季'] = df2['年'].astype(str) + df2['季'].apply(lambda x:smd[x])
        df = df.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
        df = df[[list(df)[-1]] + list(df)[:-1]]
        df2 = df2.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
        df2 = df2[[list(df2)[-1]] + list(df2)[:-1]]
        l = vstack((array([list(df)]), array(df))).transpose().tolist()
        m = df.max().max()
        list(df)

        df1 = df.copy()
        df1=df1.fillna('0')
        df1.ix[:, 1:] = df1.ix[:, 1:].replace('--', 0)
        df1.ix[:, 1:] = df1.ix[:, 1:].astype(float)
        df1.ix[:, 1:] = df1.ix[:, 1:].apply(lambda x: x / m * 100)

        for c in ['基本每股盈餘（元）', '預收股款（權益項下）之約當發行股數（單位：股）', '母公司暨子公司所持有之母公司庫藏股股數（單位：股）', '每股參考淨值', '待註銷股本股數（單位：股）']:
            try:
                pem = df[c].max()
                df1[c] = df[c].apply(lambda x: x / pem * 100)
            except:
                pass
        for i in range(len(df1)):
            for j in range(df1.shape[1]):
                try:
                    if df1.iloc[i, j]<0:
                        df1.iloc[i, j]=df1.iloc[i, j]*(-1)
                except:
                    pass
        lw = vstack((array([list(df1)]), array(df1))).transpose().tolist()
        lc = vstack((array([list(df2)]), array(df2))).transpose().tolist()
        shape(lc)
        for i in lw:
            i[0]=0.0
        for i in lc:
            i[0]='white'
        li = []
        for i in range(len(l)):
            a=['--' if isnull(a) else a for a in l[i]]    # nan/None is not allowed in javascript
            b = ['--' if isnull(b) else b for b in lw[i]]
            c = ['--' if isnull(c) else c for c in lc[i]]
            li.append([list(z) for z in list(zip(a, b, c))])
        report.append(li)
        tb.append(table)
    # [list(i) for i in list(zip([1, 2, 3], [1, 2, 3]))]

    # for j in report[0][1:]:
    #     for i in j:
    #         print(i[0],i[1],i[2])
    d['report'] = report
    d['tb'] = tb
    d['tab'] = '#tabs-8'
    print('compname:', d['compname'], 'compid_report:', d['compid_report'], 'report:', report, 'tb:', tb)
    return jsonify({'compname': d['compname'], 'compid_report': d['compid_report'], 'report': report, 'tb': tb})

# @app.route('/rep1ajax/', methods=['GET', 'POST'])
# def rep1ajax():
#     global report1, tb1, d, compid1
#     report1=[]
#     tb1=[]
#     # database = 'mops'
#     database = 'summary'
#     conn = connect('{}.sqlite3'.format(database))
#     c = conn.cursor()
#     # compid1='5522'
#     compid1 = getPostParameter(PostParameters('data'), 'compid_report1')
#     # compid1 = request.form['compid_report1']
#     d['compid_report1'] = compid1
#     print('compid_report1:', compid1)
#     # table = 'ifrs前後-綜合損益表(季)-一般業'
#     # table = 'ifrs前後-資產負債表-一般業'
#     # for table in ['ifrs前後-綜合損益表(季)', 'ifrs前後-資產負債表-一般業']:
#     for table in ['ifrs前後-綜合損益表(季)-一般業', 'ifrs前後-資產負債表-一般業']:
#         df = read_sql_query('select * from `{}` where `公司代號`="{}"'.format(table, compid1), conn)
#         df['季'] = df['季'].astype(int)
#         # if table =='ifrs前後-綜合損益表(季)':
#         if table == 'ifrs前後-綜合損益表(季)-一般業':
#             df['基本每股盈餘（元）'] = df['基本每股盈餘（元）'].map('{:,.2f}'.format)
#             col2 = {
#                 '營業成本': '&emsp;&emsp;營業成本',
#                 '未實現銷貨（損）益': '&emsp;&emsp;未實現銷貨（損）益',
#                 '已實現銷貨（損）益': '&emsp;&emsp;已實現銷貨（損）益',
#                 '營業費用': '&emsp;&emsp;營業費用',
#                 '其他收益及費損淨額': '&emsp;&emsp;其他收益及費損淨額',
#                 '營業外收入及支出': '&emsp;&emsp;營業外收入及支出',
#                 '營業外收入及利益': '&emsp;&emsp;營業外收入及利益',
#                 '所得稅費用（利益）': '&emsp;&emsp;所得稅費用（利益）',
#                 '停業單位損益': '&emsp;&emsp;停業單位損益',
#                 '合併前非屬共同控制股權損益': '&emsp;&emsp;合併前非屬共同控制股權損益',
#                 '其他綜合損益（淨額）': '&emsp;&emsp;其他綜合損益（淨額）',
#                 '合併前非屬共同控制股權綜合損益淨額': '&emsp;&emsp;合併前非屬共同控制股權綜合損益淨額',
#                 '會計原則變動累積影響數': '&emsp;&emsp;會計原則變動累積影響數'
#             }
#             df = df.rename(columns=col2)
#         d['compname1']=df.ix[len(df)-1, '公司名稱']
#         color={1:'rgb(0,255,0)', 2:'rgb(0, 190, 255)', 3:'orange', 4:'rgb(255, 75, 140)'}
#         dfColor=df.copy()
#         df3=df.copy()
#         df3.ix[:, 4:] = df3.ix[:, 4:].replace('--', 0)
#         df3.ix[:, 4:] = df3.ix[:, 4:].astype(float)
#         if table == 'ifrs前後-資產負債表-一般業':
#             col2 = {
#                 '流動資產': '&emsp;&emsp;流動資產',
#                 '非流動資產': '&emsp;&emsp;非流動資產',
#                 '基金與投資': '&emsp;&emsp;&emsp;&emsp;基金與投資',
#                 '固定資產': '&emsp;&emsp;&emsp;&emsp;固定資產',
#                 '無形資產': '&emsp;&emsp;&emsp;&emsp;無形資產',
#                 '其他資產': '&emsp;&emsp;&emsp;&emsp;其他資產',
#                 '流動負債': '&emsp;&emsp;流動負債',
#                 '非流動負債': '&emsp;&emsp;非流動負債',
#                 '長期負債': '&emsp;&emsp;&emsp;&emsp;長期負債',
#                 '各項準備': '&emsp;&emsp;&emsp;&emsp;各項準備',
#                 '其他負債': '&emsp;&emsp;&emsp;&emsp;其他負債',
#                 '股本': '&emsp;&emsp;股本',
#                 '資本公積': '&emsp;&emsp;資本公積',
#                 '保留盈餘': '&emsp;&emsp;保留盈餘',
#                 '其他權益': '&emsp;&emsp;其他權益',
#                 '庫藏股票': '&emsp;&emsp;庫藏股票',
#                 '歸屬於母公司業主之權益合計': '&emsp;&emsp;歸屬於母公司業主之權益合計',
#                 '共同控制下前手權益': '&emsp;&emsp;共同控制下前手權益',
#                 '合併前非屬共同控制股權': '&emsp;&emsp;合併前非屬共同控制股權',
#                 '非控制權益': '&emsp;&emsp;非控制權益'
#             }
#             df = df.rename(columns=col2)
#         for i in color:
#             dfColor.ix[df.季==i, 2:]=color[i]
#         smd={1:'3/31', 2:'6/30', 3:'9/30', 4:'12/31'}
#         # df['年季'] = df['年'].astype(str) + '年第' + df['季'].astype(str) + '季'
#         df['年季'] = df['年'].astype(str) + '/' + df['季'].apply(lambda x: smd[x])
#         for i in range(len(df3)):
#             for j in range(df3.shape[1]):
#                 try:
#                     if df3.iloc[i, j]<0:
#                         dfColor.iloc[i, j]='red'
#                 except:
#                     pass
#         dfColor['季'] = dfColor['季'].astype(int)
#         dfColor['年季'] = dfColor['年'].astype(str) + '/' + dfColor['季'].apply(lambda x:smd[x])
#         df = df.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
#         df = df[[list(df)[-1]] + list(df)[:-1]]
#         dfColor = dfColor.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
#         dfColor = dfColor[[list(dfColor)[-1]] + list(dfColor)[:-1]]
#         # l = vstack((array([list(df)]), array(df))).transpose().tolist()
#         df.dtypes
#         df.ix[:, 1:] = df.ix[:, 1:].replace('--', NaN)
#         df.ix[:, 1:] = df.ix[:, 1:].astype(float)
#         m = df.ix[:, 1:].max().max()
#         list(df)
#         dfWidth = df.copy()
#         dfWidth = dfWidth.fillna(0)
#         # dfWidth.ix[:, 1:] = dfWidth.ix[:, 1:].replace('--', 0)
#         # dfWidth.ix[:, 1:] = dfWidth.ix[:, 1:].astype(float)
#         dfWidth.ix[:, 1:] = dfWidth.ix[:, 1:].apply(lambda x: x / m * 100)
#
#         for c in ['基本每股盈餘（元）', '預收股款（權益項下）之約當發行股數（單位：股）', '母公司暨子公司所持有之母公司庫藏股股數（單位：股）', '每股參考淨值', '待註銷股本股數（單位：股）']:
#             try:
#                 pem = df[c].max()
#                 dfWidth[c] = df[c].apply(lambda x: x / pem * 100)
#             except:
#                 pass
#
#         for i in range(len(dfWidth)):
#             for j in range(dfWidth.shape[1]):
#                 try:
#                     if dfWidth.iloc[i, j]<0:
#                         dfWidth.iloc[i, j]=dfWidth.iloc[i, j]*(-1)
#                 except:
#                     pass
#
#         dfPercent = df.copy()
#         list(dfPercent)
#         df.dtypes
#         if table == 'ifrs前後-綜合損益表(季)-一般業':
#             for i in list(dfPercent)[2:]:
#                 dfPercent[i] = dfPercent[i] / dfPercent.營業收入 * 100
#             dfPercent.營業收入 = dfPercent.營業收入 / dfPercent.營業收入 * 100
#         if table == 'ifrs前後-資產負債表-一般業':
#             a = list(dfPercent)[1:]
#             a.remove('資產總額')
#             for i in a:
#                 dfPercent[i] = dfPercent[i] / dfPercent.資產總額 * 100
#             dfPercent.資產總額 = dfPercent.資產總額 / dfPercent.資產總額 * 100
#
#         dfPercent.ix[:, 1:] = dfPercent.ix[:, 1:].applymap('{:,.0f}'.format)
#         df = df.fillna('')
#         dfPercent = dfPercent.replace('nan', '')
#         # l = vstack((array([list(df)]), array(df))).transpose().tolist()
#         # lp = vstack((array([list(dfPercent)]), array(dfPercent))).transpose().tolist()
#         # lw = vstack((array([list(dfWidth)]), array(dfWidth))).transpose().tolist()
#         # lc = vstack((array([list(dfColor)]), array(dfColor))).transpose().tolist()
#
#         if table == 'ifrs前後-綜合損益表(季)-一般業':
#             lspan=['<span class=inc{}>sparklines</span>'.format(i) for i, j in enumerate(list(df))]
#
#             l = vstack((array([list(df)]), array(df), array([lspan]))).transpose().tolist()
#             lspan = [None for i in list(df)]
#             lp = vstack((array([list(dfPercent)]), array(dfPercent), array([lspan]))).transpose().tolist()
#             lw = vstack((array([list(dfWidth)]), array(dfWidth), array([lspan]))).transpose().tolist()
#             lc = vstack((array([list(dfColor)]), array(dfColor), array([lspan]))).transpose().tolist()
#
#             lspan=[]
#             for x in l:
#                 # print(x)
#                 lspan.append(['null' if i=='' else i for i in x])
#             l[3][2]==''
#             lspan[1]
#             lspan[1][1:-1]
#             for i in lspan[1:]:
#                 print(i[1:-1])
#             d['lspan'] = lspan
#         if table == 'ifrs前後-資產負債表-一般業':
#             lspan = ['<span class=bal{}>sparklines</span>'.format(i) for i, j in enumerate(list(df))]
#
#             l = vstack((array([list(df)]), array(df), array([lspan]))).transpose().tolist()
#             lspan = [None for i in list(df)]
#             lp = vstack((array([list(dfPercent)]), array(dfPercent), array([lspan]))).transpose().tolist()
#             lw = vstack((array([list(dfWidth)]), array(dfWidth), array([lspan]))).transpose().tolist()
#             lc = vstack((array([list(dfColor)]), array(dfColor), array([lspan]))).transpose().tolist()
#
#             lspan = []
#             for x in l:
#                 # print(x)
#                 lspan.append(['null' if i == '' else i for i in x])
#             l[3][2] == ''
#             lspan[1]
#             lspan[1][1:-1]
#             for i in lspan[1:]:
#                 print(i[1:-1])
#             d['lspan1'] = lspan
#
#         shape(lp)
#         for i in lw:
#             i[0]=0.0
#         for i in lc:
#             i[0]='white'
#         for i in lp:
#             i[0]=''
#
#         li = []
#         for i in range(len(l)):
#             li.append(zip(l[i], lw[i], lc[i], lp[i]))

#         report1.append([list(x) for x in li])
#         tb1.append(table)
#
#     li1 = []
#     for i in report1:
#         li11 = []
#         for j in i:
#             li12 = []
#             for k in j:
#                 k = list(k)
#                 k = ['NaN' if isnull(m) else m for m in k]  # nan/None are undefined in javascript
#                 print("k:", k)
#                 li12.append(k)
#             li11.append(li12)
#         li1.append(li11)
#     report2 = li1.copy()
#     # print(report2)
#     d['report1'] = report2
#     d['tb1'] = tb1
#     d['tab'] = '#tabs-9'
#     return jsonify({'lspan': d['lspan'], 'lspan1': d['lspan1'], 'compid_report1': d['compid_report1'], 'compname1': d['compname1'], 'report1': report2, 'tb1': tb1, 'tab': '#tabs-9'})
import copy
@app.route('/rep1ajax/', methods=['GET', 'POST'])
def rep1ajax():
    global incStatement, balSheet, tb1, d, compid1
    # compid1='5522'
    # table = 'ifrs前後-綜合損益表(季)-一般業'
    # table = 'ifrs前後-資產負債表-一般業'
    tb1 = {}
    database = 'summary'
    conn = connect('{}.sqlite3'.format(database))
    c = conn.cursor()
    compid1 = getPostParameter(PostParameters('data'), 'compid_report1')
    d['compid_report1'] = compid1
    print('compid_report1:', compid1)
    table = 'ifrs前後-綜合損益表(季)-一般業'
    tb1['inc'] = table
    df = read_sql_query('select * from `{}` where `公司代號`="{}"'.format(table, compid1), conn)
    df.dtypes
    col2 = {
        '營業成本': '&emsp;&emsp;營業成本',
        '未實現銷貨（損）益': '&emsp;&emsp;未實現銷貨（損）益',
        '已實現銷貨（損）益': '&emsp;&emsp;已實現銷貨（損）益',
        '營業費用': '&emsp;&emsp;營業費用',
        '其他收益及費損淨額': '&emsp;&emsp;其他收益及費損淨額',
        '營業外收入及支出': '&emsp;&emsp;營業外收入及支出',
        '營業外收入及利益': '&emsp;&emsp;營業外收入及利益',
        '所得稅費用（利益）': '&emsp;&emsp;所得稅費用（利益）',
        '停業單位損益': '&emsp;&emsp;停業單位損益',
        '合併前非屬共同控制股權損益': '&emsp;&emsp;合併前非屬共同控制股權損益',
        '其他綜合損益（淨額）': '&emsp;&emsp;其他綜合損益（淨額）',
        '合併前非屬共同控制股權綜合損益淨額': '&emsp;&emsp;合併前非屬共同控制股權綜合損益淨額',
        '會計原則變動累積影響數': '&emsp;&emsp;會計原則變動累積影響數'
    }
    df = df.rename(columns=col2)

    if len(df['公司名稱'].unique()) == 1:
        d['compname1'] = df['公司名稱'].unique()[0]
    else:
        print("len(d['compname1']) is not 1")

    floatCols = [col for col in list(df) if col not in ['年', '季', '公司代號', '公司名稱']]
    df.ix[:, floatCols] = df.ix[:, floatCols].replace('--', 0).astype(float)

    smd={1:'3/31', 2:'6/30', 3:'9/30', 4:'12/31'}
    df.insert(0, '年月日', df['年'].astype(str) + '/' + df['季'].apply(lambda x: smd[x]))
    color={1:'rgb(0,255,0)', 2:'rgb(0, 190, 255)', 3:'orange', 4:'rgb(255, 75, 140)'}
    dfColor = df.copy()
    dfColor.dtypes
    for i in color:
        dfColor.ix[df.季==i, floatCols]=color[i]

    for i in range(len(df)):
        for j in range(df.shape[1]):
            try:
                if df.iloc[i, j]<0:
                    dfColor.iloc[i, j]='red'
            except:
                pass

    df = df.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
    dfColor = dfColor.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
    dfWidth = df.copy()
    max = dfWidth[floatCols].max().max()
    dfWidth = dfWidth.fillna(0)
    dfWidth[floatCols] = dfWidth[floatCols].apply(lambda x: x / max * 100)
    df.dtypes
    for c in ['基本每股盈餘（元）']:
        try:
            pem = df[c].max()
            dfWidth[c] = df[c].apply(lambda x: x / pem * 100)
        except:
            pass

    for i in range(len(dfWidth)):
        for j in range(dfWidth.shape[1]):
            try:
                if dfWidth.iloc[i, j]<0:
                    dfWidth.iloc[i, j]=dfWidth.iloc[i, j]*(-1)
            except:
                pass

    dfPercent = df.copy()
    dfPercent.dtypes
    for i in list(dfPercent)[2:]:
        dfPercent[i] = dfPercent[i] / dfPercent.營業收入 * 100
    dfPercent.營業收入 = dfPercent.營業收入 / dfPercent.營業收入 * 100
    dfPercent.ix[:, 1:] = dfPercent.ix[:, 1:].applymap('{:,.0f}'.format) # this will convert float to object
    # df = df.fillna('')
    dfPercent = dfPercent.replace('nan', '')

    lspan=['<span class=inc{}>sparklines</span>'.format(i) for i, j in enumerate(list(df))]
    l = vstack((array([list(df)]), array(df), array([lspan]))).transpose().tolist()
    lspan = [None for i in list(df)] # None for percent, width, color
    lp = vstack((array([list(dfPercent)]), array(dfPercent), array([lspan]))).transpose().tolist()
    lw = vstack((array([list(dfWidth)]), array(dfWidth), array([lspan]))).transpose().tolist()
    lc = vstack((array([list(dfColor)]), array(dfColor), array([lspan]))).transpose().tolist()
    for i in lw:
        i[0] = 0.0
    for i in lc:
        i[0] = 'white'
    for i in lp:
        i[0] = ''

    lsparkline = []
    for x in l:
        lsparkline.append(['null' if i=='' else i for i in x])

    d['lsparkline'] = lsparkline

    incStatement = []
    for i in range(shape(l)[0]):
        row = []
        for j in range(shape(l)[1]):
            row.append({'value': l[i][j], 'width': lw[i][j], 'color': lc[i][j], 'percent': lp[i][j]})
        incStatement.append(row)
    d['incStatement'] = incStatement

    table = 'ifrs前後-資產負債表-一般業'
    tb1['bal'] = table
    df = read_sql_query('select * from `{}` where `公司代號`="{}"'.format(table, compid1), conn)
    df.dtypes
    col2 = {
        '流動資產': '&emsp;&emsp;流動資產',
        '非流動資產': '&emsp;&emsp;非流動資產',
        '基金與投資': '&emsp;&emsp;&emsp;&emsp;基金與投資',
        '固定資產': '&emsp;&emsp;&emsp;&emsp;固定資產',
        '無形資產': '&emsp;&emsp;&emsp;&emsp;無形資產',
        '其他資產': '&emsp;&emsp;&emsp;&emsp;其他資產',
        '流動負債': '&emsp;&emsp;流動負債',
        '非流動負債': '&emsp;&emsp;非流動負債',
        '長期負債': '&emsp;&emsp;&emsp;&emsp;長期負債',
        '各項準備': '&emsp;&emsp;&emsp;&emsp;各項準備',
        '其他負債': '&emsp;&emsp;&emsp;&emsp;其他負債',
        '股本': '&emsp;&emsp;股本',
        '資本公積': '&emsp;&emsp;資本公積',
        '保留盈餘': '&emsp;&emsp;保留盈餘',
        '其他權益': '&emsp;&emsp;其他權益',
        '庫藏股票': '&emsp;&emsp;庫藏股票',
        '歸屬於母公司業主之權益合計': '&emsp;&emsp;歸屬於母公司業主之權益合計',
        '共同控制下前手權益': '&emsp;&emsp;共同控制下前手權益',
        '合併前非屬共同控制股權': '&emsp;&emsp;合併前非屬共同控制股權',
        '非控制權益': '&emsp;&emsp;非控制權益'
    }
    df = df.rename(columns=col2)

    if len(df['公司名稱'].unique()) == 1:
        d['compname1'] = df['公司名稱'].unique()[0]
    else:
        print("len(d['compname1']) is not 1")

    floatCols = [col for col in list(df) if col not in ['年', '季', '公司代號', '公司名稱']]
    df.ix[:, floatCols] = df.ix[:, floatCols].replace('--', 0).astype(float)

    smd={1:'3/31', 2:'6/30', 3:'9/30', 4:'12/31'}
    df.insert(0, '年月日', df['年'].astype(str) + '/' + df['季'].apply(lambda x: smd[x]))
    color={1:'rgb(0,255,0)', 2:'rgb(0, 190, 255)', 3:'orange', 4:'rgb(255, 75, 140)'}
    dfColor = df.copy()
    dfColor.dtypes
    for i in color:
        dfColor.ix[df.季==i, floatCols]=color[i]

    for i in range(len(df)):
        for j in range(df.shape[1]):
            try:
                if df.iloc[i, j]<0:
                    dfColor.iloc[i, j]='red'
            except:
                pass

    df = df.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
    dfColor = dfColor.drop(['年', '季', '公司代號', '公司名稱'], axis=1)
    dfWidth = df.copy()
    max = dfWidth[floatCols].max().max()
    dfWidth = dfWidth.fillna(0)
    dfWidth[floatCols] = dfWidth[floatCols].apply(lambda x: x / max * 100)
    df.dtypes
    for c in ['預收股款（權益項下）之約當發行股數（單位：股）', '母公司暨子公司所持有之母公司庫藏股股數（單位：股）', '每股參考淨值', '待註銷股本股數（單位：股）']:
        try:
            pem = df[c].max()
            dfWidth[c] = df[c].apply(lambda x: x / pem * 100)
        except:
            pass

    for i in range(len(dfWidth)):
        for j in range(dfWidth.shape[1]):
            try:
                if dfWidth.iloc[i, j]<0:
                    dfWidth.iloc[i, j]=dfWidth.iloc[i, j]*(-1)
            except:
                pass

    dfPercent = df.copy()
    dfPercent.dtypes
    a = list(dfPercent)[1:]
    a.remove('資產總額')
    for i in a:
        dfPercent[i] = dfPercent[i] / dfPercent.資產總額 * 100
    dfPercent.資產總額 = dfPercent.資產總額 / dfPercent.資產總額 * 100
    dfPercent.ix[:, 1:] = dfPercent.ix[:, 1:].applymap('{:,.0f}'.format) # this will convert float to object
    # df = df.fillna('')
    dfPercent = dfPercent.replace('nan', '')

    lspan=['<span class=bal{}>sparklines</span>'.format(i) for i, j in enumerate(list(df))]
    l = vstack((array([list(df)]), array(df), array([lspan]))).transpose().tolist()
    lspan = [None for i in list(df)] # None for percent, width, color
    lp = vstack((array([list(dfPercent)]), array(dfPercent), array([lspan]))).transpose().tolist()
    lw = vstack((array([list(dfWidth)]), array(dfWidth), array([lspan]))).transpose().tolist()
    lc = vstack((array([list(dfColor)]), array(dfColor), array([lspan]))).transpose().tolist()
    for i in lw:
        i[0] = 0.0
    for i in lc:
        i[0] = 'white'
    for i in lp:
        i[0] = ''

    lsparkline = []
    for x in l:
        lsparkline.append(['null' if i=='' else i for i in x])

    d['lsparkline1'] = lsparkline

    balSheet = []
    for i in range(shape(l)[0]):
        row = []
        for j in range(shape(l)[1]):
            row.append({'value': l[i][j], 'width': lw[i][j], 'color': lc[i][j], 'percent': lp[i][j]})
            balSheet.append(row)
    d['balSheet'] = balSheet

    d['tb1'] = tb1
    d['tab'] = '#tabs-9'
    return jsonify({'incStatement':incStatement, 'balSheet':balSheet, 'lsparkline': d['lsparkline'], 'lsparkline1': d['lsparkline1'], 'compid_report1': d['compid_report1'], 'compname1': d['compname1'], 'tb1': tb1, 'tab': d['tab']})
