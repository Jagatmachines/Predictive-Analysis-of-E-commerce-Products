import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pylab as hac
import matplotlib.pyplot
import csv

from datetime import datetime

#%matplotlib inline

from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA

def main():
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

	hac.ylim(0,10)
	#hac.plot(ts)
	#hac.show()



	ts_log = np.log(ts)
	#hac.plot(ts_log)
	#hac.show()

	#moving_avg = pd.rolling_mean(ts_log,12)
	# hac.plot(moving_avg, color='red')
	# hac.plot(ts_log)
	# hac.show();

	#ts_log_moving_avg_diff = ts_log - moving_avg
	#print ts_log_moving_avg_diff.head(12)

	#ts_log_moving_avg_diff.dropna(inplace=True)

	expwighted_avg = pd.ewma(ts_log, halflife=12)
	# hac.plot(ts_log)
	# hac.plot(expwighted_avg, color='red')
	# hac.show()

	ts_log_diff = ts_log - ts_log.shift()
	#hac.plot(ts_log_diff)
	#hac.show()

	#Decomposition
	# decomposition = seasonal_decompose(ts_log)

	# trend = decomposition.trend
	# seasonal = decomposition.seasonal
	# residual = decomposition.resid

	ts_log_ewma_diff = ts_log - expwighted_avg


	#Original
	# hac.subplot(411)
	# hac.plot(ts_log, label='Original')
	# hac.legend(loc='best')

	# hac.subplot(412)
	# hac.plot(trend, label='Trend')
	# hac.legend(loc='best')
	# hac.subplot(413)
	# hac.plot(seasonal,label='Seasonality')
	# hac.legend(loc='best')
	# hac.subplot(414)
	# hac.plot(residual, label='Residuals')
	# hac.legend(loc='best')
	# hac.tight_layout()
	# hac.show()

	# lag_acf = acf(expwighted_avg, nlags=20)
	# lag_pacf = pacf(expwighted_avg, nlags=20, method='ols')

	# lag_acf = acf(ts_log_ewma_diff, nlags=20)
	# lag_pacf = pacf(ts_log_ewma_diff, nlags=20, method='ols')

	ts_diff = ts - ts.shift()

	lag_acf = acf(ts_log_diff, nlags=20)
	lag_pacf = pacf(ts_log_ewma_diff, nlags=20, method='ols')
	#lag_pacf = pacf(ts_log_ewma_diff, nlags=20)


	#Plot ACF: 
	# hac.subplot(121) 
	# hac.plot(lag_acf)
	# hac.axhline(y=0,linestyle='--',color='gray')
	# hac.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	# hac.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	# hac.title('Autocorrelation Function')

	# #Plot PACF:
	# hac.subplot(122)
	# hac.plot(lag_pacf)
	# hac.axhline(y=0,linestyle='--',color='gray')
	# hac.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	# hac.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	# hac.title('Partial Autocorrelation Function')
	# hac.tight_layout()

	#hac.show()



	#AR Model
	# model = ARIMA(ts_log, order=(2, 1, 0))
	# result_AR = model.fit(disp=-1)
	# hac.plot(ts_log_diff)
	# hac.plot(result_AR.fittedvalues, color='red')
	# hac.title('RSS: %.4f'% sum((result_AR.fittedvalues-ts_log_diff)**2))
	# hac.show()

	#MA Model
	# model = ARIMA(ts_log, order=(0, 1, 2))  
	# results_MA = model.fit(disp=-1)  
	# hac.plot(ts_log_diff)
	# hac.plot(results_MA.fittedvalues, color='red')
	# hac.title('RSS: %.4f'% sum((results_MA.fittedvalues-ts_log_diff)**2))
	# hac.show()

	#Combined
	model = ARIMA(ts_log, order=(8, 1, 1))  
	results_ARIMA = model.fit(disp=-1)  
	# hac.plot(ts_log_diff)
	# hac.plot(results_ARIMA.fittedvalues, color='red')
	# hac.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-ts_log_diff)**2))
	# hac.show()

	predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
	#print(predictions_ARIMA_diff.head())

	predictions_ARIMA_diff_cumsum =predictions_ARIMA_diff.cumsum()
	#print(predictions_ARIMA_diff_cumsum.head())

	predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
	predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
	#print(predictions_ARIMA_log.head())

	predictions_ARIMA = np.exp(predictions_ARIMA_log)
	#print predictions_ARIMA
	hac.xlabel('Month')
	hac.ylabel('Rating')
	#hac.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-ts)**2)/len(ts)))
	hac.title('Time Series Forecasting Review')
	hac.legend(loc="upper left")
	
	hac.plot(ts1)
	hac.plot(predictions_ARIMA, linestyle='--')
	hac.show()
		 
		#save figure to png
	hac.savefig("premajic.png")
	print("\nForecasting plotted")

if __name__ == "__main__":
    main()