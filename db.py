import sqlite3

dbname = 'hanbai.db'

def select():
    con = sqlite3.connect(dbname)
    con.row_factory = sqlite3.Row # 辞書型で受け取る
    cur = con.cursor()
    sql = 'SELECT * FROM shouhin'
    
    rows = []
    for row in cur.execute(sql):
        rows.append(row)

    con.commit() # 確定
    con.close()
    return rows

def find(sid):
    con = sqlite3.connect(dbname)
    con.row_factory = sqlite3.Row # 辞書型で受け取る
    cur = con.cursor()
    sql = 'SELECT * FROM shouhin WHERE sid=?'
    param = (sid,)
    row = cur.execute(sql,param).fetchone()

    con.commit() # 確定
    con.close()
    return row

def insert(sname,tanka):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    sql = "INSERT INTO shouhin (sname,tanka) VALUES (?,?)"
    
    param = (sname, tanka)
    cur.execute(sql,param) # SQL実行
    
    con.commit() # 確定
    con.close()

def delete(sid):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    sql = "DELETE FROM shouhin WHERE sid=?"
    
    param = (sid,)
    cur.execute(sql,param) # SQL実行
    
    con.commit() # 確定
    con.close()

def update(sid,sname,tanka):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    sql = "UPDATE shouhin SET sname=?,tanka=? WHERE sid=?"
    
    param = (sname, tanka,sid)
    cur.execute(sql,param) # SQL実行
    
    con.commit() # 確定
    con.close()


