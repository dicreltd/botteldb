from bottle import route, run, template
from bottle import get,post,request,redirect
import db
import uriage

@route('/')
def root():
    str = "こんにちは"
    return template('root', mes=str,mes2="おはよう")

@route('/hanbai')
def hanbai():
    rows = db.select()
    return template('hanbai', rows=rows)

@route('/shouhin',method="POST")
def shouhin():
    #sname = request.query.get('sname')
    #tanka = request.query.get('tanka')
    sname = request.forms.sname
    tanka = request.forms.tanka
    db.insert(sname,tanka)
    redirect("/hanbai")


@route('/del',method="GET")
def del_get():
    sid = request.query.sid
    row = db.find(sid)
    return template('del', row=row)

@route('/del',method="POST")
def del_post():
    sid = request.forms.sid
    db.delete(sid)
    redirect("/hanbai")

@route('/update',method="GET")
def update_get():
    sid = request.query.sid
    row = db.find(sid)
    return template('update', row=row)

@route('/update',method="POST")
def update_post():
    sid = request.forms.sid
    sname = request.forms.sname
    tanka = request.forms.tanka
    db.update(sid,sname,tanka)
    redirect("/hanbai")

@route('/uriage',method="GET")
def uriage_get():
    sid = request.query.sid
    shouhin = db.find(sid)
    rows = uriage.select(sid)
    return template('uriage', rows=rows,shouhin=shouhin)

@route('/uriage',method="POST")
def shouhin():
    sid = request.forms.sid
    kosu = request.forms.kosu
    uriage.insert(sid,kosu)
    redirect("/uriage?sid=" + sid)

run(host='localhost', port=8080, debug=True)
