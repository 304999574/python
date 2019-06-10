#! /usr/bin/env python3
import flask
from flask import render_template
import json

from stork_query import stock_check, result_parse, get_stock

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if flask.request.method == 'GET':
        result = {}
        print('get')
        return render_template("UiMain.html", result=result)
    elif flask.request.method == 'POST':

        stock_no = flask.request.form['storkcode']
        print(stock_no)
        code = stock_check(stock_no)
        if code != 0:
            result = result_parse(get_stock(code))
            print(result)
            # return render_template("UiMain.html", result=result)
            return json.dumps(result)
        else:
            return render_template("UiMain.html", warning="请输入正确的股票代码")

@app.route('/01-server')
def server():
    return render_template('Uicandlestick-sh.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)