import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pylab as haha
import matplotlib.pyplot
import csv

from datetime import datetime

#%matplotlib inline

from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA


rcParams['figure.figsize'] = 15, 6

# data = pd.read_csv('weeklyrating.csv')
# print data.head()
# print '\n Data Types:'
# print data.dtypes

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
# dateparse('1962-01')\n",
data = pd.read_csv('weeklyrating1.csv', parse_dates=['From Date'], index_col=['From Date'], date_parser=dateparse)
data1 = pd.read_csv('weeklyrating.csv', parse_dates=['To Date'], index_col=['To Date'], date_parser=dateparse)
#data1 = pd.read_csv('weeklyrating.csv', parse_dates=['From Date'], index_col=['From Date'], date_parser=dateparse)

#data = pd.read_csv('weeklyrating.csv', parse_dates=['From_Date','To_Date'], index_col=['From_Date','To_Date'], date_parser=dateparse)

#data = pd.read_csv('AirPassengers.csv', parse_dates='Month', index_col='Month',date_parser=dateparse)

# print data.index

# print data.head()

ts = data['Rating']
ts1 = data1['Rating']
#ts = data1['Rating']

#print ts.head(10)

haha.ylim(0,10)
#haha.plot(ts)
#haha.show()





#print predictions_ARIMA
haha.plot(ts1)
haha.xlabel('Weekly')
haha.ylabel('Rating')
#haha.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-ts)**2)/len(ts)))
haha.title('Weekly Rating Graph')
haha.savefig("origi.png")
print("\nRating Graph plotted")