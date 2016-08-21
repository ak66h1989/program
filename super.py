# rename table
report='投信買賣超彙總表 (股)'
key=['年月日', '證券代號']
# key=['年', '季', '公司代號']
sql='ALTER TABLE `'+ report + '` RENAME TO`' + report + '0`'
c.execute(sql)
df = read_sql_query('SELECT * from `'+report +'0`', conn).sort_values(key).drop_duplicates(key)

for y in range(93,106):
    df['年月日']=df['年月日'].replace(str(y), str(y+1911), regex=True)
# df=df.drop(['年季'], axis=1)
# df=df[['年', '季']+[col for col in df.columns if col not in ['年', '季']]]
# df['公司代號'] = df['公司代號'].astype(str).replace('\.0', '', regex=True)
# df['公司代號'], df['公司名稱'] = df['公司代號'].str.strip(), df['公司名稱'].str.strip()
df['成交統計'] = df['成交統計'].str.strip()
# df = df.drop_duplicates(['年', '季', '公司代號'])
# df = df.drop_duplicates(['年月日', '指數'])
# df=df.sort_values(['年月日', '指數'])
df = df.drop_duplicates(['年月日', '成交統計'])
df=df.sort_values(['年月日', '成交統計'])
# ----create table----
names = list(df)
c = conn.cursor()
# sql = "create table `" + report + "`(" + "'" + names[0] + "'"
# for n in names[1:len(names)]:
#     sql = sql + ',' + "'" + n + "'"
# # sql = sql + ', PRIMARY KEY (`'+key[0]+'`,`'+key[1]+'`))'
# sql = sql + ', PRIMARY KEY (`'+key[0]+'`,`'+key[1]+'`,`'+key[2]+'`))'
# c.execute(sql)
sql0=("create table `" + report + "`(" +', '.join(['`%s`'] * (len(names))))%tuple(names)
sql1=(', PRIMARY KEY(' + ', '.join(['`%s`'] * (len(key)))+'))')%tuple(key)
sql=sql0+sql1
c.execute(sql)
# ----inserting data----
sql = 'INSERT INTO `' + report +  '` VALUES (?'
n = [',?'] * (len(names) - 1)
for h in n:
    sql = sql + h
sql = sql + ')'
c.executemany(sql, df.values.tolist())
conn.commit()
print('done')

c = conn.cursor()
sql = "drop table `" + report +  "0`"
c.execute(sql)

y=['94', '95', '96', '97', '98', '99','100', '101', '102', '103', '104']
m=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
d=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

date=[]
for year in y:
    for month in m:
        for day in d:
            date.append([year, month, day])
date[-1]


industry=['銀行業','證券業','一般業','金控業','保險業','未知業']
# rename table
report='資產負債表'
# key=['年月日', '成交統計']
# key=['年', '季', '公司代號']
for ind in industry:
    sql='ALTER TABLE `'+ report +'-'+ ind +'` RENAME TO`' + report +'-'+ ind + '0`'
    c.execute(sql)

for ind in industry:
    df = read_sql_query('SELECT * from `'+report +'-'+ ind +'0`', conn)
