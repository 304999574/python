import json
import sys
import flask
from flask import request, render_template, redirect, session

from . import topic
from .stock_info import Stockinfo
from .stock_select import *
from .stork_query import result_parse, get_stock, stock_check
sys.path.append('/home/tarena/PycharmProjects/untitled/Stockv1.1/app')
# from ..manage import *

# from manage import *

@topic.route('/')
def uimain():
    return redirect("/login")

#查询单个股票
@topic.route('/stock', methods=['GET', 'POST'])
def homepage():
    # if flask.request.method == 'GET':
    #     result = {}
    #     print('get')
    #     return render_template("UiMain1.html")#result=result
    if flask.request.method == 'POST':
        stock_no = flask.request.form['storkcode']
        code = stock_check(stock_no)
        if code != 0:
            result = result_parse(get_stock(code))
            # return render_template("UiMain1.html", result=result)
            return json.dumps(result)
        else:
            return render_template("UiMain1.html") #warning="请输入正确的股票代码"

# @topic.route('/01-server')
# def server():
#     return render_template('Uicandlestick-sh.html')

# @topic.route('/02-stockinfo')
# def stock_info01():
#     return  render_template('stocktest01.html')

#查询股票视图
@topic.route('/02-stockinfo_server')
def stock_info01_server():
    stockcode=request.args['stockcode']
    sdate=request.args['starttime']
    edate=request.args['endtime']
    st1 = Stockinfo(stockcode)
    result = st1.show_stock_history(sdate, edate)
    try:
        pass
    except Exception as e:
        print(e)
        result={"text":0}

    return json.dumps(result)
#
# @topic.route('/03-stockbuy')
# def stock_buy_server():
#     stockcode= request.args['stockcode']
#     stime =request.args['stime']
#     etime=request.args['etime']

#牛股数据接口
@topic.route('/04-stocklook')
def stock_look_server():
    number1=request.args['unumber1']
    number2=request.args['unumber2']
    stock=Stock_strategy()
    if number1=='01':
        if number2=='03':
            re=stock.select_by_topcount(5)
            lists=stock.ma5_strategy(re)
        elif number2=='04':
            re = stock.select_by_topcount(5)
            lists=stock.ma20_strategy(re)
    elif number1=='02':
        if number2=='03':
            re=stock.select_by_topnet(5)
            lists=stock.ma5_strategy(re)
        elif number2=='04':
            re = stock.select_by_topnet(5)
            lists=stock.ma20_strategy(re)
    st=stock.market_condition()
    try:
        dic ={
            "status": 1,
            "text": "查询成功",
            "stcok":'现在股票市场为：'+st,
        }
    except:
        dic = {
            "status": 0,
            "text": "查询失败",
        }
    dic["lists"]=lists
    return json.dumps(dic)




































