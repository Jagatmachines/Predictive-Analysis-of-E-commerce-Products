import requests
import json
import sqlite3
import datetime
from pprint import pprint

from analyzer import Sentiment

def main():
    conn = sqlite3.connect('test.db')

    with open('bag_of_words.json') as data_file:
        datas = json.load(data_file)

    myObj = Sentiment()
    total = 0
    ident = 0
    for i, data in enumerate(datas):
        reviews = data['REVIEWS']
        for j, rev in enumerate(reviews.values()):
            review = rev['REVIEW']
            date = datetime.datetime.strptime(rev['DATE'].replace('on ', ''), "%B %d, %Y").date()
            print('{}) {}'.format(i*10+j+1, review))
            # words = myObj.bag_of_words(review)
            # rate = 0
            # count = 0
            # for word in words:
            if not review:
                rate = 5.0
            else:
                post_data = {'text': review}
                response = requests.post(url="http://text-processing.com/api/sentiment/", data=post_data)
                jsonObj = response.json()
                #     if jsonObj['label'] != 'neutral':
                #         rate += jsonObj['probability']['pos']
                #         count += 1
                # rate = rate / count * 10
                rate = jsonObj['probability']['pos'] * 10
            print("\n{}) Rate: {:.2f}\n\n".format(i*10+j+1, rate))
            cur = conn.execute("SELECT ID from RATING")
            for row in cur:
                ident = row[0]
            if ident == None:
                ident = 0
            ident += 1
            conn.execute("INSERT INTO RATING (ID, Rating, Rdate) VALUES (?, ?, ?)", [ident, rate, date])
    conn.commit()


    print ("Records created successfully")
    cursor = conn.execute("SELECT ID, Rating, Rdate from RATING")
    for row in cursor:
       print ("ID = ", row[0])
       print ("RATING = ", row[1])
       print ("RDATE = ", row[2], "\n")

    print ("Operation done successfully");

    conn.close()

        # pprint(jsonObj)
        # myprint(jsonObj)

    # def myprint(d):
    #     for k, v in d.items():
    #         if isinstance(v, dict):
    #             myprint(v)
    #         else:
    #             print("{0} : {1}".format(k, v))


