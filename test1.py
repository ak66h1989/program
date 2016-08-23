def change1(df):
    df0 = df[[x for x in list(df) if df[x].dtype == 'O']]
    df1 = df[[x for x in list(df) if df[x].dtype != 'O']]
    a0 = array(df0)
    a1 = array(df1)
    v = vstack((a1[0], a1[1:] - a1[0:len(df) - 1]))
    h = hstack((a0, v))
    return DataFrame(h, columns=list(df0) + list(df1))
from pandas import *
from numpy import *
df = DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); df
df['logic'] = where(df['AAA'] > 5,'high', nan); df