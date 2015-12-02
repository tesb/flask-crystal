#!/usr/bin/env python
# coding:utf-8

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_index():
    return render_template('index.html')


@app.route('/query/sydh/')
def tiaozhuan():
    return None



@app.route('/query/sydh/<title>/')
def func_test(title=0):
    return render_template('test.html',title = title)




if __name__ == '__main__':
    app.debug=True
    app.run()


