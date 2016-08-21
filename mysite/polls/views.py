from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from .models import Forr, Forr1

from sqlite3 import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\TEJ.sqlite3')
c = conn.cursor()

db=[]
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in range(len(c.fetchall())):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tb=c.fetchall()[i][0]
    db.append(tb)


import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
from functools import *
from pyearth import Earth
from matplotlib import pyplot

from sklearn import *

import time

forr = read_sql_query("SELECT * from `forr`", conn).replace('', nan)
ycol = ['r1']
dropcol=[j for j in ['年月日', '證券代號', 'lnr', 'lnr025', 'lnr05', 'lnr1', 'lnr2', 'lnr3', 'lnr6', 'r025', 'r05', 'r1', 'r2', 'r3', 'r6', 'r025.s', 'r05.s', 'r1.s', 'r2.s', 'r3.s', 'r6.s'] if j not in list(ycol)]
df = forr.drop(dropcol, axis=1).drop(['投信鉅額交易', '漲跌(+/-)', '外資鉅額交易'], axis=1).dropna()
# df = forr.drop(dropcol, axis=1).dropna()
y = df[ycol]
x = df[[col for col in list(df) if col not in ycol]]
df_test = df.sample(frac=0.1)
df_train = df.loc[~df.index.isin(df_test.index)]
y_train, y_test = df_train[list(y)], df_test[list(y)]
x_train, x_test = df_train[list(x)], df_test[list(x)]

h=[''.join('<th>{}</th>'.format(i) for i in list(x))]
h=''.join('<tr>{}</tr>'.format(i) for i in h)
h=''.join('<thead>{}</thead>'.format(h))
r=[]
for i in range(3000, 3100):
    c = array(round(x, 3).ix[[i,]]).tolist()[0]
    r.append(''.join('<td> {}</td>'.format(i) for i in c))
r=''.join('<tr>{}</tr>'.format(i) for i in r)
r=''.join('<tbody>{}</tbody>'.format(r))
data = h+r
table = ''.join('<table id="table_id" class="display">{}</table>'.format(data))
style = """<head>
<style>
table tr:nth-child(even) {
    background-color: #eee;
}
table tr:nth-child(odd) {
   background-color:#fff;
}
table th {
}
table td {
    text-align: right;
}
</style>
</head>"""
html = "<html>"+style+"<body>{}</body></html>" .format(table)

d=dict()

def data(request):
    firstrow=request.POST['firstrow']
    lastrow=request.POST['lastrow']
    h=[''.join('<th>{}</th>'.format(i) for i in list(x))]
    h=''.join('<tr>{}</tr>'.format(i) for i in h)
    h=''.join('<thead>{}</thead>'.format(h))
    r=[]
    for i in range(int(firstrow), int(lastrow)):
        c = array(round(x, 3).ix[[i,]]).tolist()[0]
        r.append(''.join('<td> {}</td>'.format(i) for i in c))
    r=''.join('<tr>{}</tr>'.format(i) for i in r)
    r=''.join('<tbody>{}</tbody>'.format(r))
    data=h+r
    table=''.join('<table id="table_id" class="display">{}</table>'.format(data))
    style="""<head>
    <style>
    table tr:nth-child(even) {
    background-color: #eee;
    }
    table tr:nth-child(odd) {
    background-color:#fff;
    }
    table th {
    }
    table td {
    text-align: right;
    }
    </style>
    </head>"""
    html = "<html>"+style+"<body>{}</body></html>" .format(table)
    d['table']= html
    # return HttpResponse(html)
    # d['nr']=nr
    return render(request, 'index.html', d)

def index(request):
    d['nrow'], d['row'], d['table'], d['time'], d['db'] = len(x), round(len(x)/20), table, time.time(), db
    return render(request, 'index.html', d)
    # latest_question_list = Forr1.objects.order_by('time')[:5]
    # output = ', '.join([q.time for q in latest_question_list])
    # return HttpResponse(output)

def database(request):
    global d
    global dbtables
    dbtables= request.POST.get('dbtable')
    d['dbtable']= dbtables
    conn = connect('C:\\Users\\ak66h_000\\Documents\\TEJ.sqlite3')
    df = read_sql_query('select * from `%s`'%(d['dbtable']), conn)
    d['names'] = list(df)
    # d['field'] = request.POST.getlist('field')
    return render(request, 'index.html', d)

def database1(request):
    d['dbtable']= dbtables
    d['field'] = request.POST.getlist('field')
    return render(request, 'index.html', d)

def mars(request):
    #----mars----
    model = Earth()
    model.fit(x_train, y_train)
    t=str(model.trace())
    s=model.summary()
    d['trace'], d['summary'] = t, s
    # if 'score_bic' in globals():
    #     d = {'table':table,'trace': t, 'summary': s, 'model_bic_score': score_bic, 'time': time.time()}
    #     return render(request, 'index.html', d)
    # else:
    #     d = {'table':table,'trace': t, 'summary': s, 'time': time.time()}
    #     return render(request, 'index.html', d)
    return render(request, 'index.html', d)
    #----lasso----
    # return render(request, 'index.html', d)
def brt(request):
    #----gbm----
    from sklearn.cross_validation import KFold
    # Fit classifier with out-of-bag estimates
    params = {'n_estimators': 1000, 'max_depth': 4, 'subsample': 0.5,
              'learning_rate': 0.01, 'min_samples_leaf': 1, 'verbose':1}
    clf = ensemble.GradientBoostingRegressor(**params)
    clf.fit(x_train, y_train)
    acc = clf.score(x_test, y_test)
    print("Accuracy: {:.4f}".format(acc))
    n_estimators = params['n_estimators']
    x = np.arange(n_estimators) + 1
    def heldout_score(clf, x_test, y_test):
        score = np.zeros((n_estimators,), dtype=np.float64)
        for i, y_pred in enumerate(clf.staged_predict(array(x_test))):  # staged_predict() can only be run after fit
            score[i] = clf.loss_(array(y_test), y_pred)
        return score

    def cv_estimate(n_folds=4):
        cv = KFold(n=x_train.shape[0], n_folds=n_folds, shuffle=True)  # KFold is not random without shuffle=True
        cv_clf = ensemble.GradientBoostingRegressor(**params)
        val_scores = np.zeros((n_estimators,), dtype=np.float64)
        for train, test in cv:
            cv_clf.fit(array(x_train)[train], array(y_train)[train])   # need use array
            val_scores += heldout_score(cv_clf, array(x_train)[test], array(y_train)[test])  # need use array
        return val_scores

    # Estimate best n_estimator using cross-validation
    cv_score = cv_estimate(4)

    # Compute best n_estimator for test data
    clf = ensemble.GradientBoostingRegressor(**params)
    clf.fit(x_train, y_train)
    test_score = heldout_score(clf, x_test, y_test)*10

    # min loss according to OOB
    oob_best_iter = x[np.argmin(clf.train_score_)]

    # min loss according to test
    test_best_iter = x[np.argmin(test_score)]

    # min loss according to cv
    cv_best_iter = x[np.argmin(cv_score)]

    feature_importance = clf.feature_importances_
    # # make importances relative to max importance
    # feature_importance = 100.0 * (feature_importance / feature_importance.max())
    sorted_idx = np.argsort(feature_importance)
    # pos = np.arange(sorted_idx.shape[0]) + .5
    # plt.subplot(1, 2, 2)
    # plt.barh(pos, feature_importance[sorted_idx], align='center')
    # plt.yticks(pos, array(list(x_train))[sorted_idx], fontproperties=zhfont1)
    # plt.xlabel('中文', fontproperties=zhfont1)
    # plt.title('Variable Importance')
    # plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    # plt.show()

    from bokeh.plotting import figure, show, output_file, vplot
    from bokeh.models import Span
    p2 = figure()
    p2.line(np.arange(n_estimators) + 1, clf.train_score_*2, legend="OOB loss")
    p2.line(np.arange(n_estimators) + 1, cv_score, legend="cv loss", line_color="green")
    p2.line(np.arange(n_estimators) + 1, test_score, legend="test loss", line_color="orange")
    vline1 = Span(location=oob_best_iter, dimension='height', line_color='blue',line_dash='dashed', line_width=2)
    vline2 = Span(location=cv_best_iter, dimension='height', line_color='green',line_dash='dashed', line_width=2)
    vline3 = Span(location=test_best_iter, dimension='height', line_color='orange',line_dash='dashed', line_width=2)
    p2.renderers.extend([vline1, vline2, vline3])

    factors = array(list(x_train))[sorted_idx].tolist()
    x = feature_importance[sorted_idx].tolist()
    p1 = figure(title="feature_importance", tools="resize,save", y_range=factors, x_range=[min(x), max(x)])
    p1.segment(0, factors, x, factors, line_width=2)

    from bokeh.embed import components
    script, div= components((p1, p2))
    # d = {'table':table, 'script': script, 'div_p1': div[0], 'div_p2': div[1],}
    d['script'], d['div_p1'], d['div_p2'], d['time']=script, div[0], div[1], time.time()
    return render(request, 'index.html', d)

def lasso(request):
    #----lasso----
    from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
    model_bic = LassoLarsIC(criterion='bic', verbose=True)
    model_bic.fit(x_train, y_train)
    alpha_bic_ = model_bic.alpha_
    # global score_bic
    score_bic = model_bic.score(x_test, y_test)
    t1 = time.time()
    # d=dict()
    # if 'summary' in globals():
    #     d = {'trace': t, 'summary': s, 'model_bic_score': score_bic, 'time': time.time(),}
    #     return render(request, 'index.html', d)
    # if 'score_aic' in globals():
    #     d = {'table':table,'model_bic_score': score_bic, 'time': time.time(), 'model_aic_score': score_aic,}
    #     return render(request, 'index.html', d)
    # else:
    #     d = {'table':table,'model_bic_score': score_bic, 'time': time.time(),}
    #     return render(request, 'index.html', d)
    # d = {'model_bic_score': score_bic, 'time': time.time(),}
    # return render(request, 'index.html', d)
    #----lasso----
    d['score_bic'], d['time'] = score_bic, time.time()
    return render(request, 'index.html', d)


def lasso_aic(request):
    #----lasso----
    from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
    model_aic = LassoLarsIC(criterion='aic')
    model_aic.fit(x_train, y_train)
    alpha_aic_ = model_aic.alpha_
    # global score_aic
    score_aic = model_aic.score(x_test, y_test)
    t1 = time.time()
    # d=dict()
    # if 'summary' in globals():
    #     d = {'trace': t, 'summary': s, 'model_bic_score': score_bic, 'time': time.time(),}
    #     return render(request, 'index.html', d)
    # if 'score_bic' in globals():
    #     d = {'table':table,'model_bic_score': score_bic, 'time': time.time(), 'model_aic_score': score_aic,}
    #     return render(request, 'index.html', d)
    # else:
    #     d = {'table':table,'model_aic_score': score_aic, 'time': time.time(),}
    #     return render(request, 'index.html', d)
    # d = {'model_aic_score': score_aic, 'time': time.time(),}
    d['score_aic'], d['time'] = score_aic, time.time()
    return render(request, 'index.html', d)
    
    
def test(request):
    l = request.POST.getlist('user_name[]')
    print(l)
    return render(request, 'index.html', {'test':l})






