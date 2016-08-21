import psycopg2
conn = psycopg2.connect("dbname=tse user=postgres password=d03724008")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("CREATE TABLE test1 (id serial PRIMARY KEY, 數字 integer, data varchar);")
cur.execute("CREATE TABLE 測試 (id serial PRIMARY KEY, 數字 integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
cur.execute("INSERT INTO test1 (數字, data) VALUES (%s, %s)",(100, "abc'def"))
cur.execute("INSERT INTO 測試 (數字, data) VALUES (%s, %s)",(100, "中文"))
cur.execute("SELECT * FROM 測試;")
cur.fetchall()
conn.commit()
cur.close()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=公開資訊觀測站 user=postgres password=d03724008")
cur = conn.cursor()

# ----create table----
names = list(df1)
sql = "create table " + dic[key] + "(" +  names[0]
for n in names[1:len(names)]:
    sql = sql + ' varchar,' + n
sql = sql + ' varchar, PRIMARY KEY (年季, 公司代號))'
cur.execute(sql)
conn.commit()

#----inserting data----
names = list(df)
sql = 'INSERT INTO ' + '綜合損益表' + ' VALUES (%s'
n = [',%s'] * (len(names) - 1)
for h in n:
    sql = sql + h
sql = sql + ')'
cur.executemany(sql, df1.values.tolist())
conn.commit()

cur.execute("SELECT * FROM 綜合損益表;")
cur.fetchone()
cur.fetchall()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
sql[400:]
len(sql)
df1 = read_sql_query("SELECT * from 綜合損益表", conn)
df1.to_sql('綜合損益表', conn, schema=None, if_exists='fail', index=False, index_label=None)


