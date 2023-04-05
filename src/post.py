"""
Bottle micro web-framework for Python.
"""
from bottle import route, run

@route('/post')
def submit_post():
    return f"Comment posted to timeline successfully..."

@route('/post/get')
def get_post():
    return "All posts in current timeline"

run(host='localhost', port=8080)
