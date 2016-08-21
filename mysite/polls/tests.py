from django.test import TestCase

# Create your tests here.


import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
from functools import *

# def mymerge(x, y):
#     m = merge(x, y, how='outer')
#     return m
def mymerge(x, y):
    m = merge(x, y, on=[col for col in list(x) if col in list(y)], how='outer')
    return m

#----test connection----
#2015
YEAR='2015'
df1=DataFrame()
SEASON='2'
url='http://localhost:8000/polls/database/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0', 'Cookie':"csrftoken=r3kRHJlu4RBPYUMU1w5Dzxwkl3MErKQs", 'Connection':"keep-alive"}
payload = {'dbtable':'forr'}
source_code = requests.post(url,headers=headers,data=payload) #should use data instead of params
source_code.encoding = 'big5'
plain_text = source_code.text
print(plain_text)