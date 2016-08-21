from django.shortcuts import render

from django.http import HttpResponse
from .models import Forr1
from datetime import datetime
from pandas import *
from sklearn import tree
from sklearn.tree import export_graphviz
import subprocess
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn import *

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })
# def home(request):
#     post_list = Forr1.objects.all().values
#     forr = DataFrame.from_records(post_list)
#
#     ycol = ['r1']
#     dropcol=[j for j in ['年月日', '證券代號', 'lnr', 'lnr025', 'lnr05', 'lnr1', 'lnr2', 'lnr3', 'lnr6', 'r025', 'r05', 'r1', 'r2', 'r3', 'r6', 'r025.s', 'r05.s', 'r1.s', 'r2.s', 'r3.s', 'r6.s'] if j not in list(ycol)]
#     df = forr.drop(dropcol, axis=1).drop(['投信鉅額交易', '漲跌(+/-)', '外資鉅額交易'], axis=1).dropna()
#     # df = forr.drop(dropcol, axis=1).dropna()
#     y = df[ycol]
#     x = df[[col for col in list(df) if col not in ycol]]
#     df_test = df.sample(frac=0.1)
#     df_train = df.loc[~df.index.isin(df_test.index)]
#     y_train, y_test = df_train[list(y)], df_test[list(y)]
#     x_train, x_test = df_train[list(x)], df_test[list(x)]
#     #----tree----
#     cv = KFold(n=x.shape[0], n_folds=10, shuffle=True)
#     params = {'min_samples_split': 9} # unlike R, complexity parameter is not supported in sklearn
#     clf = tree.DecisionTreeRegressor(**params)
#     clf.fit(x_train, y_train)
#     clf.fit(x, y)  # the result is not the same compared to r, perhaps sklearn does not use cross validation !!!
#     clf.tree_.node_count
#     score=clf.score(x,y)
#
#     return render(request, 'home.html', {
#         'score': score,
#     })

