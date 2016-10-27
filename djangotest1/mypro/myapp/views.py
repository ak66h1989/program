from django.http import HttpResponse

from django.shortcuts import render, redirect
# from pandas import *   # can not import, don't know why?
from sqlite3 import *
import os
path='C:/Users/ak66h_000/Documents/db/'
os.chdir(path)

database='mops'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
mops= []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    mops.append(tb)

database='mysum'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
mysum= []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    mysum.append(tb)

database='summary'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
summary= []
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb = c.fetchall()[i][0]
    summary.append(tb)

database='tse'
conn = connect('{}.sqlite3'.format(database))
c = conn.cursor()
tse= []
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

d = dict()

# def test(request):
#     l = request.POST.getlist('choice')   #list object
#     for i in l:
#         print(i)
#     return render(request, 'myapp/index.html', {'l': l})

def test(request):
    d['mops'], d['mysum'], d['summary'], d['tse'] = mops, mysum, summary, tse
    # dbtable = request.POST.getlist('dbtable')  #list object, empty is allowed
    # conn = connect('{}.sqlite3'.format(dic[dbtable]))
    # c = conn.cursor()
    # df = read_sql_query("SELECT * from `{}`".format(dbtable), c)
    # d['fields'] = list(df)
    l = request.POST.getlist('choice')   #list object, empty is allowed
    d['l'] = l
    for i in l:
        print(i)
    return render(request, 'myapp/testlist.html', d)

def listfield(request):
    dbtable = request.POST['dbtable']  #string object, empty is not allowed
    conn = connect('{}.sqlite3'.format(dic[dbtable]))
    # df = read_sql_query("SELECT * from `{}`".format(dbtable), conn)
    # d['fields'] = list(df)
    return render(request, 'myapp/testlist.html', d)

def index(request):
    d['db'] = db
    return render(request, 'myapp/index.html', d)
