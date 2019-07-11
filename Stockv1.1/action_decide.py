"""
stock action decide,money calculate
"""
import gugu as gg
from decimal import Decimal

class Action_decide():

    def __init__(self,stockcode,money_total,stime,etime,money_remain,stockunit=0):
        self.stockcode=stockcode
        self.money_total = money_total
        self.stime = stime
        self.etime = etime
        self.money_remamin=money_remain
        self.stockunit=stockunit


    def buy_by_smaller_price(self,price):
        """

        :param price: 当价格小于price买入
        :return:  买入股票数字，
        """
        stockhistory = gg.StockData(self.stockcode).history(self.stime,self.etime)

        result = stockhistory.loc[stockhistory['close'] < price].iloc[1]['close']
        date = stockhistory.loc[stockhistory['close'] < price].iloc[1]['date']
        price=float(result)
        print(price,date)
        self.stockunit = int(self.money_total/price//100*100)
        self.money_remain = int(self.money_total-self.stockunit*price)
        return (self.stockunit,self.money_remain,price,date)


    def cal_money_and_profit(self,stockunit,money_remain,sdate):

        stockhistory = gg.StockData(self.stockcode).history(sdate, self.etime)
        print(sdate)
        pricelist = stockhistory['close'].tolist()
        datelist = stockhistory['date'].tolist()
        outputlist = []
        for i in range(len(datelist)):
            profit = (money_remain+stockunit*pricelist[i]-self.money_total)/self.money_total
            value = Decimal(1+profit).quantize(Decimal('0.00'))
            value=str(value)
            print(value)
            listdata = [datelist[i],value]
            outputlist.append(listdata)
        result = stockhistory.iloc[-1:]['close']
        price = int(result)
        self.money_remain = self.money_remain+price*self.stockunit
        self.stockunit =0
        return [outputlist,self.money_remain]



action1 =  Action_decide('600101',1000000,"2019-01-02","2019-05-09",1000000,0)
tuple1 = action1.buy_by_smaller_price(10.2)
print(tuple1)

tuple2 = action1.cal_money_and_profit(tuple1[0],tuple1[1],tuple1[3])
print(tuple2)



