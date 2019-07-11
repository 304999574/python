import gugu as gg
import tushare as ts
from decimal import Decimal
import numpy as np
import pandas as pd
from hmmlearn import hmm








class Stock_strategy():
    def __init__(self):
        pass

    def select_by_topcount(self,topcount):
        """
        龙虎榜次数选股
        :param topcount: 龙虎榜出现次数
        :return: 股票代码列表
        """
        StockClass = gg.BillBoard()
        StockList = StockClass.countTops(topcount)
        SelectedStock = StockList.sort_values(by="count", ascending=False).head(15)
        stockcode_list = SelectedStock['code'].tolist()
        stockcode_name = SelectedStock['name'].tolist()
        result_list = []
        for i in range(len(stockcode_list)):
            list01= [stockcode_list[i],stockcode_name[i]]
            result_list.append(list01)
        return result_list

    def select_by_topnet(self,topcount):
        """
        龙虎榜买入额选股
        :param topcount: 上榜以后的净买入量
        :return: 股票列表代码
        """
        StockClass = gg.BillBoard()
        StockList = StockClass.countTops(topcount)
        SelectedStock = StockList.sort_values(by="net", ascending=False).head(5)
        stockcode_list = SelectedStock['code'].tolist()
        stockcode_name = SelectedStock['name'].tolist()
        result_list = []
        for i in range(len(stockcode_list)):
            list01 = [stockcode_list[i], stockcode_name[i]]
            result_list.append(list01)
        return result_list

    def ma5_strategy(self,result_list):
        selected_stock_list=[]
        for onestock in result_list:
            stockdata = ts.get_hist_data(onestock[0]).sort_values(by='date')
            ma5today = stockdata['ma5'].iloc[-1:].values[0]
            ma5yesday = stockdata['ma5'].iloc[-2:].values[0]
            ma10today = stockdata['ma10'].iloc[-1:].values[0]
            price = float(ma5today)*1.03
            buyprice=str(Decimal(price).quantize(Decimal('0.00')))
            if ma5today>ma5yesday and ma5today>ma10today:
                selected_stock_list.append([onestock[0],onestock[1],buyprice])
        # print(selected_stock_list)

        return selected_stock_list

    def ma20_strategy(self,stockcode_list):
        selected_stock_list = []
        print(stockcode_list)
        for onestock in stockcode_list:
            stockdata = ts.get_hist_data(onestock[0]).sort_values(by='date')
            ma20today = stockdata['ma20'].iloc[-1:].values[0]
            ma20yesday = stockdata['ma20'].iloc[-2:].values[0]
            ma5today = stockdata['ma5'].iloc[-1:].values[0]
            price = float(ma20today)*1.03
            buyprice = str(Decimal(price).quantize(Decimal('0.00')))
            if ma20today>ma20yesday and ma5today>ma20today:
                selected_stock_list.append([onestock[0], onestock[1], buyprice])
        # print(selected_stock_list)
        return selected_stock_list



# s1 = Stock_strategy()
# result = s1.select_by_topcount(5)
# s1.ma5_strategy(result)
# s1.ma20_strategy(result)



    def market_condition(self):
        data = ts.get_hist_data('sh', start='2009-01-01', end='2019-06-24')
        volume = data['volume']
        close = data['close']

        logDel = np.log(np.array(data['high'])) - np.log(np.array(data['low']))
        logRet_1 = np.array(np.diff(np.log(close)))
        logRet_5 = np.log(np.array(close[5:])) - np.log(np.array(close[:-5]))
        logVol_5 = np.log(np.array(volume[5:])) - np.log(np.array(volume[:-5]))

        # 保持所有的数据长度相同
        logDel = logDel[5:]
        logRet_1 = logRet_1[4:]
        close = close[5:]

        Date = pd.to_datetime(data.index[5:])
        A = np.column_stack([logDel, logRet_5, logVol_5])

        model = hmm.GaussianHMM(n_components=6, covariance_type="full", n_iter=2000).fit(A)
        hidden_states = model.predict(A)
        hshow = hidden_states.tolist()
        statenumber1 = hshow[-1]
        statenumber2 = hshow[25]
        statenumber3 = hshow[10]
        statenumber4 = hshow[30]
        result_list = []
        for i in hshow:
            if i == statenumber2 or i == statenumber1:
                result_state = '牛市'
            elif i == statenumber3 or i == statenumber4:
                result_state = '熊市'
            else:
                result_state = '震荡市'
            result_list.append(result_state)
        result_list.reverse()
        market_state = result_list[-1]

       # plt.figure(figsize=(25, 18))
        # for i in range(n):
        #     pos = (hidden_states == i)
        #     plt.plot_date(Date[pos], close[pos], 'o', label='hidden state %d' % i, lw=2)
        #     plt.legend()
        # plt.show()
        #
        # res = pd.DataFrame({'Date': Date, 'logReg_1': logRet_1, 'state': hidden_states}).set_index('Date')
        # series = res.logReg_1

        # templist = []
        # plt.figure(figsize=(25, 18))
        # for i in range(n):
        #     pos = (hidden_states == i)
        #     pos = np.append(1, pos[:-1])
        #     res['state_ret%d' % i] = series.multiply(pos)
        #     data_i = np.exp(res['state_ret%d' % i].cumsum())
        #     templist.append(data_i[-1])
        #     plt.plot_date(Date, data_i, '-', label='hidden state %d' % i)
        #     plt.legend()
        # plt.show()
        #
        # templist = np.array(templist).argsort()
        # long = (hidden_states == templist[-1]) + (hidden_states == templist[-2])  # 买入
        # short = (hidden_states == templist[0]) + (hidden_states == templist[1])  # 卖出
        # long = np.append(0, long[:-1])
        # short = np.append(0, short[:-1])
        #
        # plt.figure(figsize=(25, 18))
        # res['ret'] = series.multiply(long) - series.multiply(short)
        # plt.plot_date(Date, np.exp(res['ret'].cumsum()), 'r-')
        # plt.show()
        return market_state


if __name__== "__main__":
    s1 = Stock_strategy()
    # stocklist =s1.select_by_topcount(topcount=5)
    # print(stocklist)
    # stocklist = ['000693', '300775', '300615', '600401', '002070']
    #
    # stockcode = stocklist[1]
    # print(stockcode)
    # sdata = ts.get_hist_data(stockcode)
    # sdata =sdata.sort_values(by='date')
    # print(sdata)
    # ma5today = sdata['ma5'].iloc[-1:].values[0]
    # ma5yesday = sdata['ma5'].iloc[-2:].values[0]
    # print(ma5today,ma5yesday)
    # print('-----------')

    # s1 = Stock_strategy()
    # stocklist = s1.select_by_topnet(5)
    # selection = s1.ma20_strategy(stock
    print(s1.market_condition())