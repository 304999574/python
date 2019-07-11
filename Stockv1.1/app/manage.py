#! /user/bin/env python3
#启动和项目管理的相关代码

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
# 连接到MySQL中flaskDB数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/UsersDB"
# 指定不需要信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 指定程序的启动模式为调试模式
app.config['DEBUG'] = True
# 指定执行完增删改之后的自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
#设置秘钥
app.config['SECRET_KEY']='SDJKsdfDKSLGsdafASDKS'
# 创建SQLAlchemy的实例
db = SQLAlchemy(app)
#创建Manager对象并指定要管理的app
manager = Manager(app)

#创建Migrate对象,并指定关联的app和db
migrate = Migrate(app,db)

#为manager增加数据库的迁移指令
#为manager增加一个子命令-db(自定义),具体操作由MigrateCommand来提供
manager.add_command('db',MigrateCommand)

#根据数据库编写所有的实体类
#导入 db 到models.py
from app.topic import topic as topic_blueprint

app.register_blueprint(topic_blueprint)
# 将users蓝图程序与app关联到一起
from app.users import users as users_blueprint

app.register_blueprint(users_blueprint)

#通过db创建实体类

# 创建用户信息表
class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer,primary_key=True)#编号
    uname = db.Column(db.String(32),nullable=False,unique=True,index=True)#账户名
    upwd = db.Column(db.String(64),nullable=True)#密码
    userTime = db.Column(db.DateTime)
    vipTime = db.Column(db.DateTime)#ｖｉｐ时间
    avaMoney = db.Column(db.DECIMAL(16,2),default=0)#金钱
    stockMoney = db.Column(db.DECIMAL(16,2),default=0)#股票价值
    amt = db.Column(db.DECIMAL(16,2),default=0)#总价值
    path=db.Column(db.String(128),default='../static/images/4.png')#头像路径名
    def to_dict(self):
        dic = {
            "id": self.uid,
            "uname": self.uname,
            "upwd": self.upwd,
            "avaMoney":self.avaMoney,
            "stockMoney":self.stockMoney,
            "vipTime": self.vipTime.strftime('%Y年%m月%d日') if self.vipTime!=None else None,
            "amt":self.amt,
            "path":self.path
        }
        return dic


class Stock(db.Model):
    __tablename__ = "stock"
    sid = db.Column(db.Integer,primary_key=True)#
    sname = db.Column(db.String(128),nullable=False,index=True)#股票名
    snumber = db.Column(db.String(64),nullable=False)#股票号码
    buyTime = db.Column(db.DateTime)#买入时间
    sellTime = db.Column(db.DateTime,default=None)#卖出时间
    shands = db.Column(db.Integer)#持股数量
    price = db.Column(db.DECIMAL(6,2))#买入时价格
    isActive = db.Column(db.Boolean,default=True)#是否显示

    users = db.relationship(
        "User",
        secondary = "user_stock",
        lazy = "dynamic",
        backref = db.backref(
            "stocks",
            lazy = "dynamic"
        )
    )


class UserStock(db.Model):
    __tablename__ = "user_stock"
    usid = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.Integer,db.ForeignKey("user.uid"))
    sid = db.Column(db.Integer,db.ForeignKey("stock.sid"))


if __name__ == "__main__":
    manager.run()


























