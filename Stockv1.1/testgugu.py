import gugu as gg
import pandas as pd
import matplotlib.pyplot as plt
print (gg.__version__)

# obj= gg.MarketData()
# data = obj.index()
# obj.output()
# StockClass=gg.BillBoard()
# StockList=StockClass.countTops(5)
# print(StockList)
# print(StockList.describe())
# SelectedStock=StockList.sort_values(by="count",ascending=False).head(5)
# print(SelectedStock)
# Stockcode=SelectedStock['code'].values
# print(Stockcode)
# for i in Stockcode:
# Stockhistory=gg.StockData('600100').history('2019-04-13','2019-05-13')
# print(Stockhistory)
Stockbigdatalist = gg.StockData('600100').bigDeal(date='2019-6-11')
stockname = Stockbigdatalist['name'].tolist()[0]
print(stockname)
#     Stockhistory.plot(x="date",y="close")
#     plt.show()
# print(Stockcode[1])
# code1 = Stockcode[1]
# StockTick = gg.StockData(code1).todayTicks()
# print(StockTick)
# Stockhistory=gg.StockData(Stockcode[0]).history('2019-04-13','2019-05-13')
# print(Stockhistory)
# Stockhistory=gg.StockData("600100").history('2019-04-13','2019-05-13')
# result = Stockhistory.loc[Stockhistory['close']<12.3].iloc[1]['close']
# print(result)
# result=str(result)
# print(type(result))