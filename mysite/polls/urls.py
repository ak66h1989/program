from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
    url(r'^database/$', views.database, name='db'),
    url(r'^database1/$', views.database, name='db1'),
    url(r'^data/$', views.data, name='data'),
    url(r'^$', views.index, name='index'),
    url(r'^mars/$', views.mars, name='mars'),
    url(r'^lasso/$', views.lasso, name='lasso'),
    url(r'^lasso_aic/$', views.lasso_aic, name='lasso_aic'),
    url(r'^brt/$', views.brt, name='brt'),
    url(r'^test/$', views.test, name='test'),

]

# urlpatterns = [
#     url(r'^data$', views.data, name='data'),
#     url(r'^$', views.lasso, name='lasso'),
#     url(r'^$', views.index, name='index'),
#     url(r'^$', views.mars, name='mars'),
#
# ]