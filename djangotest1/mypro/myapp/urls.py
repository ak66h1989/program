from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^test/$', views.test, name='test'),
    url(r'^listfield/$', views.listfield, name='listfield'),
    url(r'^listfield1/$', views.listfield1, name='listfield1'),
    url(r'^listfield2/$', views.listfield2, name='listfield2'),
    url(r'^query/$', views.query, name='query'),
    url(r'^mline/$', views.mline, name='mline'),
    url(r'^scale/$', views.scale, name='scale'),
    url(r'^mp/$', views.mp, name='mp'),
    url(r'^plot/$', views.plot, name='plot'),
    url(r'^plot1/$', views.plot1, name='plot1'),
    url(r'^ys/$', views.ys, name='ys'),
    url(r'^remove/$', views.remove, name='remove'),
    url(r'^changeall/$', views.changeall, name='changeall'),
    url(r'^c3/$', views.c3, name='c3'),
    url(r'^rep/$', views.rep, name='rep'),
    url(r'^rep1/$', views.rep1, name='rep1'),
    url(r'^datatable/$', views.datatable, name='datatable'),
    url(r'^bokeh/$', views.bokeh, name='bokeh'),
]