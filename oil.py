import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

futures=pd.read_csv("oil futures.csv")
futures=futures[["Previous","Unnamed: 10"]]
futures.columns=["price",'date']
futures=futures.dropna(how="any")
futures=futures.iloc[0:8,:]
futures.date=futures.date.map(lambda x: datetime.datetime.strptime(x,'%m/%d/%Y'))
futures=futures.set_index("date",drop=True)

prices=pd.read_csv("WTI prices.csv",sep="\t")
col_names=["date","time","open","high","low","close","tickvol","vol","spread"]
prices.columns=col_names
prices=prices[['date','close','time']]
prices.date=prices.date.astype(str)+prices.time.astype(str)
prices.date=prices.date.map(lambda x: datetime.datetime.strptime(x,'%Y.%m.%d%H:%M:%S'))
prices=prices[['date','close']]

fig, ((ax1, ax2)) = plt.subplots(2, 1)
#fig.suptitle('Lambda derivatives plots')
ax1.plot(prices.date, prices.close)
ax1.set_title('WTI price', fontsize=8)
ax1.set( ylabel='Price')


ax2.plot(futures.resample('h').interpolate('quadratic'))
ax2.set_title('CLM20 (Crude Oil WTI Futures) ', fontsize=8)
ax2.set( ylabel='Futures price')

#plt.setp( ax1.xaxis.get_majorticklabels(), rotation=-15 )
#plt.setp( ax2.xaxis.get_majorticklabels(), rotation=-15)
#plt.locator_params(axis='x', nbins=4)

fig.tight_layout(pad=1.0)


every_nth = 2
for n, label in enumerate(ax1.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
for n, label in enumerate(ax2.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)











