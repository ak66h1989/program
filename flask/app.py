# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 09:43:49 2016

@author: ak66h_000
"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
    
@app.route('/test', methods=['GET'])
def index():
    return '''<form action="/test" method="post">
              <input type="text" name="username" value='1'>
              <input type="text" name="username" value='2'>
              <p><button type="submit">run</button></p>
              </form>'''

@app.route('/test', methods=['POST'])
def test():
    print(request.form.getlist('username'))
    return '{}'.format(request.form.getlist('username'))  # only text type can get value


if __name__ == '__main__':
    app.run()