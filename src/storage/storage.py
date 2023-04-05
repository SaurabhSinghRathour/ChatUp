"""
Bottle micro web-framework for Python.
"""
from bottle import route, run, redirect
import time

DB = []

@route('/post')
def submit_post():
    print(time.ctime())
    DB.append(time.ctime())
    print(time.ctime())
    return redirect("http://localhost:7070/")
    #return f"Comment posted to timeline successfully..."

@route('/post/get')
def get_post():
    print(time.ctime())
    return str(DB)

run(host='localhost', port=8080)
