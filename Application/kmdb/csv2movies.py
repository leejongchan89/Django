import sqlite3

import pandas as pd # pip install pandas

csv_file = './data/kmdb_get_movie_list_100_new.csv'
df = pd.read_csv(csv_file)

conn = sqlite3.connect('./../mydatabase.sqlite3') # 접속 객체
cursor = conn.cursor() # cursor 객체는 SQL 쿼리를 데이터베이스에 전달하고, 쿼리의 결과를 가져오는 등의 작업을 수행

# movies 테이블을 생성하는 문장입니다. (필요에 따라 데이터 타입을 지정)
sql = '''
create table if not exists movies(
    movieCd integer primary key autoincrement,
    movieNm text,
    movieNmEn text,
    prdtYear real,
    openDt real,
    typeNm text,
    prdtStatNm text,
    nationAlt text,
    genreAlt text,
    repNationNm text,
    repGenreNm text
)
'''

cursor.execute(sql)

df.to_sql('movies', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print('데이터 베이스 파일에 데이터 추가를 성공하였습니다.')