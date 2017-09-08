import requests
import json
from pprint import pprint

from analyzer import Sentiment


with open('bag_of_words.json') as data_file:
    datas = json.load(data_file)


myObj = Sentiment()
total = 0
for i, data in enumerate(datas):
    reviews = data['REVIEWS']

    j = 1
    print(i)
    review = reviews[str(i)]['REVIEW']
    print('{}) {}'.format(j, review))
    # words = myObj.bag_of_words(review)
    # rate = 0
    # count = 0
    # for word in words:
    post_data = {'text': review}
    response = requests.post(url="http://text-processing.com/api/sentiment/", data=post_data)
    jsonObj = response.json()
    #     if jsonObj['label'] != 'neutral':
    #         rate += jsonObj['probability']['pos']
    #         count += 1
    # rate = rate / count * 10
    rate = jsonObj['probability']['pos'] * 10
    total += rate
    print("\n{}) Rate: {:.2f}\n\n".format(j, rate))
    j += 1

avg = total/len(datas)
print("{}) Final Rating: {:.2f}".format(i, avg))

    # pprint(jsonObj)
    # myprint(jsonObj)

# def myprint(d):
#     for k, v in d.items():
#         if isinstance(v, dict):
#             myprint(v)
#         else:
#             print("{0} : {1}".format(k, v))