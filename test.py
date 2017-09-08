#import amazonscrapt
from analyzer import Sentiment
import rough
import ratinggen
#import jsut
import sqlite
import createtable
import predict
import tocsv
import piechart
import predweek


# # myObj.train([myObj.get_positive_data() for _ in range(10)], [myObj.get_negative_data() for _ in range(10)])

# # pos = myObj.get_positive_data()
# # print('\nPositive Review:\n', pos)
# # print('Filtered Words:\n', myObj.bag_of_words(pos))
# # neg = myObj.get_negative_data()
# # print('\nNegative Review:\n', neg)
# # print('Filtered Words:\n', myObj.bag_of_words(neg))

# # print('\nPrediction: ', myObj.predict([pos, neg]))

# test = ['This is very good', 'This is bad', 'This is awesome', 'It is the worst', "It's boring"]
# for i in test:
#     print('{}: {}'.format(i, myObj.predict(i)))


#amazonscrapt.ReadAsin()
myObj = Sentiment()



def main():
	
	sqlite.main()
	createtable.main()
	myObj.main()
	rough.main()
	ratinggen.main()
	predict.main()
	#jsut.main()
	piechart.main()
	tocsv.main()
	predweek.main()
