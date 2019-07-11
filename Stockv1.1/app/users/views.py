
import datetime,time
import json
import os
# import sys
# sys.path.append('/home/tarena/PycharmProjects/untitled/Stockv1.1/app')
# from manage import *
import decimal
from flask import render_template, request, make_response, session, redirect

from ..manage import *
from . import users


#注册返回的网址
@users.route('/register')
def register():
    if request.method == "GET":
        return render_template("UIregister1.html")

#登录返回的网址
@users.route('/loginregister')
def login_register():
    return render_template("UiLogin1.html")

#登录ajax判断账户名
@users.route('/checkuname')
def checkuname():
    uname = request.args['uname']
    user = User.query.filter_by(uname=uname).first()
    if user:
        dic = {
            "status":1,
            "text":"已存在用户"
        }
    else:
        dic = {
            "status":0,
            "text":"可以使用账户名"
        }
    return json.dumps(dic)

#登录判断注册是否成功
@users.route('/server',methods=['POST'])
def server():
    user = User()
    user.uname = request.form['uname']
    user.upwd = request.form['upwd']
    user.userTime = datetime.datetime.now()
    try:
        db.session.add(user)
        db.session.commit()
        dic = {
            "status":1,
            "text":"注册成功",
        }
    except Exception as e:
        print(e)
        dic = {
            "status":0,
            "text":"注册失败"
        }
    return json.dumps(dic)

#退出用户
@users.route('/delect')
def delect():
    if 'usession' in session:
        resp = make_response("<script>location.href='/login'</script>")
        resp.delete_cookie('uname')
        session.pop('usession')
        return resp
    return redirect('/login')

#主页面与账户信息登录
@users.route('/login',methods=['GET','POST'])
def login():
    user={"uname":"未登录", "vipTime":"普通账户","avaMoney":"0.00",'stockMoney':'0.00',"amt":"0.00","path":"../static/images/4.png"}
    if request.method == 'GET':
        if 'usession' in session:
            uname=session['usession']
            user1=User.query.filter_by(uname=uname).first()
            if not user1:
                user = {"uname": "未登录", "vipTime": "普通账户", "avaMoney": "0.00",'stockMoney':'0.00', "amt": "0.00","path":"../static/images/4.png"}
                return render_template("UiMain1.html", parms=locals())
            user=user1.to_dict()

            return render_template("UiMain1.html", parms=locals())

        else:
            #判断cookeis中是否有 uname
            if 'uname' in request.cookies:
                #判断uname的值
                uname = request.cookies['uname']
                user1 = User.query.filter_by(uname=uname).first()
                if user:
                    session['usession'] = uname
                    user=user1.to_dict()

                    return render_template("UiMain1.html", parms=locals())
                else:
                    resp = make_response()
                    resp.delete_cookie('uname')

            user = {"uname": "未登录", "vipTime": "普通账户", "avaMoney": "0.00",'stockMoney':'0.00', "amt": "0.00","path":"../static/images/4.png"}
            return render_template("UiMain1.html", parms=locals())
    else:
        #接收用户名和密码并判断是否正确
        uname = request.form['uname']
        upwd = request.form['upwd']
        user = User.query.filter_by(uname=uname).filter_by(upwd=upwd).first()
        if user:
            #登录成功
            dic = {
                "status": 1,
                "text": "登录成功"
            }

            session['usession'] = uname
            #判断是否要记住密码
            if request.form['left'] == 'true':
                #同时传送json和返回cookie
                dic=json.dumps(dic)
                resp = make_response(dic)
                resp.set_cookie('uname',uname,60*60*24*31)
                return resp
            return json.dumps(dic)
        else:
            dic = {
                "status": 0,
                "text": "登录失败"
            }
            return json.dumps(dic)

#对用户提交的ｖｉｐ进行加判断
def funtime(time,unumber,utime):

    if utime == '月':
        Nmbertime = (time + datetime.timedelta(days=unumber * 31))
    else:
        Nmbertime = (time + datetime.timedelta(days=unumber * 366))
    return Nmbertime
#vip充值
@users.route('/recharge',methods=['POST'])
def vip():
    uname=request.form['uname']
    utime=request.form['time']#月份还是年份
    unumber=int(request.form['number'])#多少个月或多少年
    user=User.query.filter_by(uname=uname).first()
    if user:#查询到用户
        time = datetime.datetime.now()#现在的时间
        usertime = user.vipTime #数据库的时间
        if usertime == None:
            usertime = (time+datetime.timedelta(days=-10))

        if time > usertime:#现在的时间超过vip时间 过期后重新充值 and 未充值过的新用户
            Nmbertime1 = funtime(time, unumber, utime)
            user.vipTime = Nmbertime1
        elif time <= usertime:#现在的时间小于vip时间　未过期继续充值
            Nmbertime2 = funtime(usertime,unumber, utime)
            user.vipTime=Nmbertime2
        # time = time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            db.session.add(user)
            db.session.commit()
            dic={
                "status": 1,
                "text": "充值成功",
                "time": user.vipTime.strftime('%Y年%m月%d日'),
                "exe":"至尊账户"
            }
        except Exception as e:
            print(e)
            dic = {
                "status": 0,
                "text": "充值失败"
            }
        return json.dumps(dic)
    else:#未查询到用户
        dic={
            "status": 0,
            "text": "充值失败"
        }

        return json.dumps(dic)

#金钱充值
@users.route('/update_data',methods=['POST'])
def money():
    uname=request.form['uname']
    umoney=int(request.form['umoney'][1:])
    user=User.query.filter_by(uname=uname).first()
    if user:
        money=user.avaMoney#取出的账户资金
        moneys=user.amt#取出的总资产
        user.avaMoney=money+umoney
        user.amt=moneys+umoney
        try:
            dic = {
                "status": 1,
                "text": "充值成功",
                "umoney": "%s"%user.avaMoney,
                "uamt": "%s"%user.amt,
            }
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            dic = {
                "status": 0,
                "text": "充值失败"
            }
        return json.dumps(dic)
    else:
        dic = {
            "status": 0,
            "text": "没有此账户"
        }
        return json.dumps(dic)





# @users.route('/trade')
# def trade():
#     """实现用户的买入和卖出活动并更新数据库用户资产数据,返回'交易成功'或者'交易失败'"""
#     # 获取view提交的用户购买股票对应的数量和价格
#     price = request.form['price'] # 交易价格
#     amount = request.form['amount'] # 交易股票数量
#
#     # 从数据库获取用户id,原可用资金,原持股数量
#     user = User.query.filter_by(uname=uname).first()
#     avaMoney = user.avaMoney # 原可用资金
#
#     stk = Stock.query.filter_by(sid = user.stock.sid).first()
#     scount = stk.scount # 原持股数量
#
#     # 判断用户活动是买入还是卖出
#     if request.form['status'] == 'buy':
#         user.avaMoney = avaMoney - price * amount # 剩余可用资金=原可用资金-购买股票的消费总金额
#         user.amt = (scount + amount) * price + user.avaMoney # 资产总值=当前持股总数*当前交易股价+剩余可用资金
#         # 更新股票购买时间,股票数量
#         stk.buyTime = datetime.datetime.now()
#         stk.scount = scount + amount
#
#     else:
#         user.avaMoney = user.avaMoney + price * amount  # 剩余可用资金=原可用资金+售出股票所得总金额
#         user.amt = (scount - amount) * price + user.avaMoney # 资产总值=当前持股总数*当前交易股价+剩余可用资金
#         # 更新股票售出时间,股票数量
#         stk.sellTime = datetime.datetime.now()
#         stk.scount = scount - amount
#
#     # 更新股票名称和股票代码
#     stk.sname = request.form['sname']
#     stk.snumber = request.form['snumber']
#
#     try:
#         # 将变更后的数据写入数据库
#         db.session.add(user)
#         db.session.add(stk)
#         dic = {
#             "status": 1,
#             "text": "交易成功",
#         }
#     except Exception as e:
#         dic = {
#             "status": 0,
#             "text": "交易失败"
#         }
#
#     return json.dumps(dic)



#股票买入
@users.route('/05-stockbuy',methods=['POST'])
def stock_buy_server():
    if request.method=="POST" and  'usession' in session:
        uname = session['usession']#用户id
        money=request.form['money'][:-1]#花费多少钱
        stockname=request.form['stockname']#股票名称
        stocknumber=request.form['stocknumber']#股票号码
        shands=request.form['shands']#股票数量
        price=request.form['stockprice'][:-3]#股票数量
        user1=User.query.filter_by(uname=uname).first()
        #查询该用户的是否买入股票
        # list=[]
        # stocks=user1.stocks.all()
        # for i in stocks:
        #     list.append(i.sname)
        # #已经买入该股票
        # if stocknumber in list:
        #     stock=Stock.query.filter_by(sname=stockname).frist()
        #     stock = Stock()
        #     stock.sname = stockname
        #     stock.snumber = stocknumber
        #     stock.shands = shands
        #     stock.buyTime = datetime.datetime.now()  # 买入时间
        # #没有买入该股票
        # else:
        stock=Stock()
        stock.sname=stockname
        stock.snumber=stocknumber
        stock.shands=shands
        stock.price=price
        stock.buyTime=datetime.datetime.now()#买入时间

        #购买金钱数小于账户资金
        if user1.avaMoney<decimal.Decimal(money):
            dic = {
                "status": 0,
                "text": "充值失败,余额不足请充值在购买",
            }
            return json.dumps(dic)
        user1.avaMoney=user1.avaMoney-decimal.Decimal(money)#购买后的资金
        user1.stockMoney=user1.stockMoney+decimal.Decimal(money)#股票价值
        try:
            db.session.add(user1)
            db.session.add(stock)
            user1.stocks.append(stock)
            db.session.commit()
            dic = {
                "status": 1,
                "text": "充值成功",
                "umoney": "%s" % user1.avaMoney,
                "stockMoney": "%s" % user1.stockMoney,
                "uamt": "%s" % user1.amt,
            }
        except:
            dic = {
                "status": 0,
                "text": "充值失败",
            }
        return json.dumps(dic)
    else:
        dic = {
            "status": 0,
            "text": "充值失败",
        }
        return json.dumps(dic)

#股票查询
@users.route('/06-stocklook',methods=['POST'])
def stocklook():
    if request.method=="POST" and 'usession' in session:#
        uname = session['usession']#用户id
        user2=User.query.filter_by(uname=uname).first()
        if user2:
            stocks=user2.stocks.filter_by(isActive=True).all()
            dic={
                "status": 1,
                "text": "查询成功",
            }
            list = []
            for i in stocks:
                l=[]
                l.append(i.sname)
                l.append(i.snumber)
                l.append(str(i.buyTime))
                l.append(i.shands)
                l.append(str(i.price))
                list.append(l)
            dic['list']=list
            return json.dumps(dic)
        else:
            dic = {
                "status": 0,
                "text": "没有该用户",
            }
            return json.dumps(dic)

# 上传头像
@users.route('/upload_profile_photo', methods= ['POST'])
def upload_head():
    if request.method == "POST" and 'usession' in session:
        uname = session['usession']
        user1=User.query.filter_by(uname=uname).first()
        if user1:
            sb = request.files['file-input']
            file=sb.read()
            with open('/home/tarena/PycharmProjects/untitled/Stockv1.1/app/static/images/img/%s'%uname+'.png','wb') as f:#../static/images/img/
                f.write(file)
            user1.path='../static/images/img/%s'%uname+'.png'
            db.session.add(user1)
            db.session.commit()
            # img='../users/img/%s'%(uname+'jpg')

            return "<script>alert('上传成功');location.href='/login';</script>"
        else:
            return "<script>alert('没有此账户，不能上传头像');location.href='/login';</script>"
    else:
        return "<script>alert('您未登录，不能上传头像');location.href='/login';</script>"




