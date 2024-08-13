import sqlite3

import pandas as pd

csv_file = './data/coffeeList.csv'
df = pd.read_csv(csv_file)

conn = sqlite3.connect('./../mydatabase.sqlite3') # 접속 객체
cursor = conn.cursor()

sql = '''
create table if not exists coffees(
    id integer primary key autoincrement,
    brand text,
    name text,
    address text,
    sido text,
    gungu text,
    latitude real,
    longitude real
)
'''

cursor.execute(sql)

df.to_sql('coffees', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print('데이터 베이스 파일에 데이터 추가를 성공하였습니다.')