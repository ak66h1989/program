from sqlite3 import *
import os
os.chdir('C:/Users/ak66h_000/Documents/db/')
# os.chdir('D:\\')
conn = connect('mysum.sqlite3')
c = conn.cursor()

import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
from functools import *

#-*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msjh.ttc')  #show chinese

get_option("display.max_rows")
get_option("display.max_columns")
set_option("display.max_rows", 1000)
set_option("display.max_columns", 1000)
set_option('display.expand_frame_repr', False)
set_option('display.unicode.east_asian_width', True)
# forr = read_sql_query("SELECT * from `forr`", conn).replace('', nan)
forr = read_sql_query("SELECT * from `forweb`", conn).replace('', nan)

from sklearn import *
ycol = ['r1']
dropcol=[j for j in ['年月日', '證券代號', 'lnr', 'lnr025', 'lnr05', 'lnr1', 'lnr2', 'lnr3', 'lnr6', 'r025', 'r05', 'r1', 'r2', 'r3', 'r6', 'r025.s', 'r05.s', 'r1.s', 'r2.s', 'r3.s', 'r6.s'] if j not in list(ycol)]
df = forr.drop(dropcol, axis=1).drop(['臺灣企業經營101報酬指數','臺灣企業經營101指數','漲升股利100報酬指數','漲升股利100指數','漲升股利150報酬指數','漲升股利150指數','小型股300報酬指數','小型股300指數','臺指日報酬兩倍指數',
'電子類兩倍槓桿指數','電子類反向指數','臺指日報酬反向一倍指數','投信鉅額交易', '漲跌(+/-)', '外資鉅額交易','ushadow/span','lshadow/span','ushadow/span_1','lshadow/span_1'], axis=1).dropna()
list(df)
len(df)
len(forr)
round(df)
df.applymap(lambda x: round(x, 4))
forr.drop(dropcol, axis=1).tail(500)


# df = forr.drop(dropcol, axis=1).dropna()
y = df[ycol]
x = df[[col for col in list(df) if col not in ycol]]
df_test = df.sample(frac=0.1)
df_train = df.loc[~df.index.isin(df_test.index)]
y_train, y_test = df_train[list(y)], df_test[list(y)]
x_train, x_test = df_train[list(x)], df_test[list(x)]

#----tree----
from sklearn import tree
from sklearn.tree import export_graphviz
import subprocess
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
cv = KFold(n=x.shape[0], n_folds=10, shuffle=True)
params = {'min_samples_split': 9} # unlike R, complexity parameter is not supported in sklearn
clf = tree.DecisionTreeRegressor(**params)
clf.fit(x_train, y_train)
clf.fit(x, y)  # the result is not the same compared to r, perhaps sklearn does not use cross validation !!!
clf.tree_.node_count
clf.score(x,y)
clf.apply(x)
len(clf.apply(x))

n_folds=10
cv = KFold(n=x_train.shape[0], n_folds=n_folds, shuffle=True)
l=[]
for n in range(2, 1000, 4):
    params = {'max_leaf_nodes': n}
    clf = tree.DecisionTreeRegressor(**params)
    score = sum(-cross_val_score(clf, x_train, y_train, cv=cv, scoring='mean_squared_error'))  # sklearn put '-' in front of mse
    R2 = 1-score/y_train.var()
    print('max_leaf_nodes : %i | mse : %.3f | R2 : %.3f' % (n, score, R2))
    l.append(score)
print(np.argmin(l)+1, l[np.argmin(l)])
params = {'max_leaf_nodes': np.argmin(l)+1}

# l=[]
# for n in range(2, 1000, 2):
#     params = {'max_leaf_nodes': n}
#     u = 0
#     for train, test in cv:
#         clf = tree.DecisionTreeRegressor(**params)
#         clf.fit(array(x_train)[train], array(y_train)[train])
#         # score += clf.score(array(x_train)[test], array(y_train)[test])
#         u += sum((array(y_train)[test] - clf.predict(array(x_train)[test]))**2)
#     v = sum((array(y_train)-array(y_train).mean())**2)
#     score = 1 - u/v
#     l.append(score)
#     print('max_leaf_nodes : %i | n_node : %.3f | R-square: %.3f' % (n, clf.tree_.node_count, score))
# print(np.argmax(l)+1, l[np.argmax(l)])
# params = {'max_leaf_nodes': np.argmax(l)+1}
clf = tree.DecisionTreeRegressor(**params)
clf.fit(x_train, y_train)
print('clf.tree_.node_count : ', clf.tree_.node_count, 'nrow : ', len(df))
testr2 = clf.score(x_test, y_test)
print('test R2 : ', testr2)
clf.predict(array(x)[-1])

import os
from graphviz import Source
os.getcwd()
#----export_graphviz----
def visualize_tree(tree, feature_names):
    with open("dt.dot", 'w') as f:
        tree.fit(x, y)
        export_graphviz(tree, out_file=f, feature_names=feature_names)
    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")
visualize_tree(clf, list(x_train))
print('finish')

file = open('dt.dot', 'r') #READING DOT FILE
text=file.read()
src = Source(text)
src.format = 'svg'
src.render('graph_tree/tree'+forr['證券代號'][0]+list(y)[0]+'Rsq'+str(format(round(testr2, 5), '.5g')), view=True)
# clf.feature_importances_
# clf.tree_
# clf.get_params()

#----mars----
import numpy
from pyearth import Earth
from matplotlib import pyplot

#Fit an Earth model
model = Earth()
model.fit(x_train, y_train)

#Print the model
print(model.trace())
print(model.summary())

#Plot the model
y_hat = model.predict(x_train)
pyplot.figure()
pyplot.plot(x_train.ix[:, 6], y_train, 'r.')
pyplot.plot(x_train.ix[:, 6], y_hat, 'b.')
pyplot.xlabel('x_6')
pyplot.ylabel('y')
pyplot.title('Simple Earth Example')
pyplot.show()
error = array(y_test) - model.predict(array(x_test))
print('R^2', 1-error.std()/y_test.var())
model.predict([array(x)[-1]])

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

# color brew for the three curves
oob_color = list(map(lambda x: x / 256.0, (190, 174, 212)))
test_color = list(map(lambda x: x / 256.0, (127, 201, 127)))
cv_color = list(map(lambda x: x / 256.0, (253, 192, 134)))

# plot curves and vertical lines for best iterations
plt.plot(x, clf.train_score_*2, label='OOB loss', color=oob_color)
plt.plot(x, test_score, label='Test loss', color=test_color)
plt.plot(x, cv_score, label='CV loss', color=cv_color)
plt.axvline(x=oob_best_iter, color=oob_color)
plt.axvline(x=test_best_iter, color=test_color)
plt.axvline(x=cv_best_iter, color=cv_color)

# add three vertical lines to xticks
xticks = plt.xticks()
xticks_pos = np.array(xticks[0].tolist() + [oob_best_iter, cv_best_iter, test_best_iter])
xticks_label = np.array(list(map(lambda t: int(t), xticks[0])) + ['OOB', 'CV', 'Test'])
ind = np.argsort(xticks_pos)
xticks_pos = xticks_pos[ind]
xticks_label = xticks_label[ind]
plt.xticks(xticks_pos, xticks_label)

plt.legend(loc='upper right')
plt.ylabel('normalized loss')
plt.xlabel('number of iterations')
plt.tight_layout()
plt.show()

# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.title('Deviance')
# plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',label='Training Set Deviance')
# plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-', label='Test Set Deviance')
# plt.legend(loc='upper right')
# plt.xlabel('Boosting Iterations')
# plt.ylabel('Deviance')
# # Plot feature importance
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
vline3 = Span(location=test_best_iter, dimension='height', line_color='orange', line_dash='dashed', line_width=2)
output_file("gbm.html")
p2.renderers.extend([vline1, vline2, vline3])
show(p2)

factors = array(list(x_train))[sorted_idx].tolist()
x = feature_importance[sorted_idx].tolist()

p1 = figure(title="feature_importance", tools="resize,save", y_range=factors, x_range=[min(x), max(x)])

p1.segment(0, factors, x, factors, line_width=2)
# p1.segment(0, factors, x, factors, line_width=2, line_color="green", )
# p1.circle(x, factors, size=15, fill_color="orange", line_color="green", line_width=3, )

# factors = ["foo", "bar", "baz"]
# x = ["foo", "foo", "foo", "bar", "bar", "bar", "baz", "baz", "baz"]
# y = ["foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"]
# colors = [
#     "#0B486B", "#79BD9A", "#CFF09E",
#     "#79BD9A", "#0B486B", "#79BD9A",
#     "#CFF09E", "#79BD9A", "#0B486B"
# ]
#
# p2 = figure(title="Categorical Heatmap", tools="resize,hover,save",
#     x_range=factors, y_range=factors)
#
# p2.rect(x, y, color=colors, width=1, height=1)
#
# output_file("categorical.html", title="categorical.py example")
output_file("feature_importance.html")
show(p1)
# show(vplot(p1, p2))  # open a browser

#----lasso----
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
model_bic = LassoLarsIC(criterion='bic', verbose=True)
t1 = time.time()
model_bic.fit(x_train, y_train)
t_bic = time.time() - t1
alpha_bic_ = model_bic.alpha_
model_bic.score(x_test, y_test)

model_aic = LassoLarsIC(criterion='aic')
model_aic.fit(x_train, y_train)
alpha_aic_ = model_aic.alpha_
model_aic.score(x_test, y_test)

model_cv = LassoCV(verbose=True)
model_cv.fit(x_train, y_train)
alpha_cv_ = model_cv.alpha_
model_cv.score(x_test, y_test)

model_Larscv = LassoLarsCV(verbose=True)
model_Larscv.fit(x_train, y_train)
alpha_Larscv_ = model_Larscv.alpha_
model_Larscv.score(x_test, y_test)

def plot_ic_criterion(model, name, color):
    alpha_ = model.alpha_
    alphas_ = model.alphas_
    criterion_ = model.criterion_
    plt.plot(-alphas_, criterion_, '--', color=color, label='%s criterion' % name)
    plt.axvline(-alpha_, color=color, label='alpha: %s estimate' % name)
    plt.xlabel('-alpha')
    plt.ylabel('criterion')

plt.figure()
plot_ic_criterion(model_aic, 'AIC', 'b')
plot_ic_criterion(model_bic, 'BIC', 'r')
plt.legend()
plt.title('Information-criterion for model selection (training time %.3fs)'% t_bic)
plt.tight_layout()
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
#----graphviz----
from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)
dot.render('test-output/round-table.gv', view=True)
from graphviz import Graph

g = Graph(format='png')
dot.format = 'svg'

dot.render()
dot = Digraph(name='pet-shop', node_attr={'shape': 'plaintext'})

dot.node('parrot')
dot.node('dead')
dot.edge('parrot', 'dead')

dot.graph_attr['rankdir'] = 'LR'
dot.edge_attr.update(arrowhead='vee', arrowsize='2')

print(dot.source)


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

n_angles = 36
n_radii = 8

# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = np.linspace(0.125, 1.0, n_radii)

# An array of angles
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# Repeat all angles for each radius
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Pringle surface
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)

plt.show()

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
re.search(r'\d\d\d-\d\d\d-\d\d\d\d','My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


cd C:\Users\ak66h_000\OneDrive\webscrap\mysite
python manage.py shell
import django
django.setup()
from polls.models import Question, Choice
Choice.objects.all()
from django.utils import timezone
q = Choice(choice_text="What's new?1", votes=1, question_id=1)
q.save()

from bokeh import *
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

from bokeh.plotting import figure
from bokeh.embed import components

plot = figure()
plot.circle([1,2], [3,4])
html = file_html(plot, CDN, "my plot")
print(html)
show(plot)

html = file_html(plot, CDN, "my plot")

plot = figure()
plot.circle([1,2], [3,4])

script, div = components(plot)
print(script)
print(div)
import os
os.getcwd()
os.listdir()
