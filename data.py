import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
CO_ID='5522'
stat=1
#2015
YEAR='2015'
df1=DataFrame()
for SEASON in ['3','2','1']:
    url = "http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID="+CO_ID+'&SYEAR='+YEAR+'&SSEASON='+SEASON+'&REPORT_ID=C'
    source_code = requests.get(url)
    source_code.encoding = 'big5'
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    h=[]
    for th in soup.find_all('table')[stat].find_all('tr')[0].find_all('th'):
        h.append(th.string)
    row=len(soup.find_all('table')[stat].find_all('tr')[2].find_all('td',{'align':""}))
    td=soup.find_all('table')[stat].find_all('tr')[2].find_all('td')
    l=[]
    for j in range(0,len(h)):
        x=[h[j]]
        for i in range(0, row*len(h),len(h)):
            x.append(td[i+j].string)
        l.append(x)
    df = DataFrame(l)
    df.columns=df.ix[0,:]
    df=df.ix[1:len(df),:]
    df1 = df1.append(df,ignore_index=True)
#2014-2012
df2=DataFrame()
for YEAR in ['2014','2013']:

    for SEASON in ['4','3','2','1']:
        url = "http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID="+CO_ID+'&SYEAR='+YEAR+'&SSEASON='+SEASON+'&REPORT_ID=C'
        source_code = requests.get(url)
        source_code.encoding = 'big5'
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        h=[]
        for th in soup.find_all('table')[stat].find_all('tr')[0].find_all('th'):
            h.append(th.string)
        row=len(soup.find_all('table')[stat].find_all('tr')[2].find_all('td',{'align':""}))
        td=soup.find_all('table')[stat].find_all('tr')[2].find_all('td')
        l=[]
        for j in range(0,len(h)):
            x=[h[j]]
            for i in range(0, row*len(h),len(h)):
                x.append(td[i+j].string)
            l.append(x)
        df = DataFrame(l)
        df.columns=df.ix[0,:]
        df=df.ix[1:len(df),:]
        df1 = df1.append(df,ignore_index=True)
    df2=df2.append(df1,ignore_index=True)
print(df2)
