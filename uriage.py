import sqlite3
from datetime import date

dbname = 'hanbai.db'

def select(sid):
    con = sqlite3.connect(dbname)
    con.row_factory = sqlite3.Row # 辞書型で受け取る
    cur = con.cursor()
    sql = 'SELECT * FROM uriage WHERE sid=?'
    param = (sid,)

    rows = []
    for row in cur.execute(sql,param):
        rows.append(row)

    con.commit() # 確定
    con.close()
    return rows

def insert(sid,kosu):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    sql = "INSERT INTO uriage (sid,kosu,hi) VALUES (?,?,?)"

    param = (sid, kosu,date.today())
    cur.execute(sql,param) # SQL実行

    con.commit() # 確定
    con.close()
