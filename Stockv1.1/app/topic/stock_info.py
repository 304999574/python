import gugu as gg
import matplotlib.pyplot as plt
from decimal import Decimal

class Stockinfo():
    def __init__(self,stockcode):
        self.stockcode = stockcode


    def show_stock_history(self,stime,etime):
        """
        查看个股历史数据
        :param stime: 必须为XXXX-XX-XX格式
        :param etime: 必须为XXXX-XX-XX格式
        :return: 个股历史数据，为list格式
        """
        Stockhistory = gg.StockData(self.stockcode).history(stime,etime)
        listdate = Stockhistory['date'].tolist()
        Stockname = gg.StockData(self.stockcode).bigDeal(date='2019-6-12')['name'].tolist()[0]


        listopen=Stockhistory['open'].tolist()
        listclose =Stockhistory['close'].tolist()
        listhigh=Stockhistory['high'].tolist()
        listlow = Stockhistory['low'].tolist()


        listdata=[]
        for i in range(len(listclose)):
            sopen=float(Decimal(listopen[i]).quantize(Decimal('0.00')))
            sclose=float(Decimal(listclose[i]).quantize(Decimal('0.00')))
            shigh=float(Decimal(listhigh[i]).quantize(Decimal('0.00')))
            slow=float(Decimal(listlow[i]).quantize(Decimal('0.00')))
            stockdaydata=[listdate[i],sopen,sclose,slow,shigh]
            listdata.append(stockdaydata)
        listdata.append([Stockname])

        return listdata
    def show_stock_tick(self):
        """
        查看当天成交数据
        :return: 个股历史数据，为dataframe格式
        """
        StockTick = gg.StockData(self.stockcode).todayTicks()
        StockTick.sort_values(by='time',ascending=True)
        StockTick.plot(x="time",y="price")
        plt.show()
        return StockTick

# st1=Stockinfo("600100")
# result = st1.show_stock_history('2019-04-13','2019-05-13')
#
#
# print(result)

# st2 = Stockinfo("600111")
# result = st2.show_stock_tick()
# print(result)


