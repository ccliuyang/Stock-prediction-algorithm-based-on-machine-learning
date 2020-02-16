import tushare as ts
import pandas as pd
import numpy as np

sz50 = ts.get_hist_data(code='sz50', start='2019-03-04', end='2019-09-29').sort_index(ascending=True)

print(sz50)
a = [0.9891, 0.9471, 0.9739, 0.9668, 1.0639, 1.0618, 1.0514999999999999, 1.0498999999999998, 1.0912999999999997, 1.0249, 1.0251, 1.0031999999999999, 1.0534999999999999, 1.0568999999999997, 1.0360999999999998, 1.0514999999999999, 1.0917999999999999, 1.1329999999999998, 1.0830999999999997, 1.0673, 1.0597999999999999, 1.1006999999999998, 1.0476999999999999, 1.0618999999999998, 1.0995, 1.1354999999999997, 1.1310999999999998, 1.1311999999999998, 1.1197, 1.1170999999999998]
b = [0.9976016059730929, 0.9539339297034584, 0.994991899697119, 0.9573078819468901, 1.0187433964922166, 1.0432732267380431, 1.0301225611044587, 1.046168204550257, 1.0352222300486018, 0.9878988518701134, 0.965383531732056, 0.956339367472001, 0.9587694583362681, 0.9660702965415228, 0.9661794745368739, 0.9839050503627526, 1.0387828414453757, 1.057596675353948, 1.0204655913221103, 1.0222617454391774, 1.0149679509755583, 1.0320807212791434, 0.9814467845319432, 0.9948580686060435, 1.0133232373036556, 1.0084806649292104, 1.0195675142635767, 1.0500774811579912, 1.0503803620483199, 1.0322286398534901]

datelist = ['2019-03-04', '2019-03-11', '2019-03-18', '2019-03-25',
            '2019-04-01', '2019-04-08', '2019-04-15', '2019-04-22', '2019-04-29',
            '2019-05-06', '2019-05-13', '2019-05-20', '2019-05-27',
            '2019-06-03', '2019-06-10', '2019-06-17', '2019-06-24',
            '2019-07-01', '2019-07-08', '2019-07-15', '2019-07-22', '2019-07-29',
            '2019-08-05', '2019-08-12', '2019-08-19', '2019-08-26',
            '2019-09-02', '2019-09-09', '2019-09-16', '2019-09-23']

start = sz50['open'].iloc[0]
rate_list = []
rate = 0.00
for i in range(0, len(datelist)):
    date = datelist[i]
    temp = sz50['close'].loc[sz50.index == date]
    temp = temp.iloc[0]
    rate = temp / start
    rate_list.append(rate)
print(rate_list)