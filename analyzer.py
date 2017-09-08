import nltk
import json
from nltk.corpus import stopwords, wordnet, movie_reviews
from nltk.stem import WordNetLemmatizer

# from glob import glob
# import os.path
# import pickle
import random
import numpy as np
import re
import collections


class Sentiment:
    def __init__(self, pos=None, neg=None):
        if not pos:
            # self.__pos = [open(f).read() for f in glob('review_polarity/txt_sentoken/pos/*.txt')]
            self.__pos = [movie_reviews.raw(file) for file in movie_reviews.fileids('pos')]
        else:
            self.__pos = pos
        if not neg:
            # self.__neg = [open(f).read() for f in glob('review_polarity/txt_sentoken/neg/*.txt')]
            self.__neg = [movie_reviews.raw(file) for file in movie_reviews.fileids('neg')]
        else:
            self.__neg = neg

        # if os.path.isfile('classifier.pickle'):
        #     # Load the features
        #     with open('classifier.pickle', 'rb') as f:
        #         self.__classifier = pickle.load(f)
        # else:
        #     # Train a data set
        #     self.__classifier = nltk.NaiveBayesClassifier.train(self.__train_data())

        #     # Cache the features for faster predictions
        #     with open('classifier.pickle', 'wb') as f:
        #         pickle.dump(self.__classifier, f)

    def __get_tag(self, tag):
        if tag.startswith('R'):
            return 'r'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('J'):
            return 'a'
        return 'n'

    def __process_chunk(self, chunk):
        subtree = [(w[0], self.__get_tag(w[1])) for w in chunk]

        # Convert to base words
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(*w) for w in subtree]

        # Handle anomalies
        words = [w.replace("n't", 'not').replace("'", '') for w in lemmas]

        # Remove stop words
        stop_words = stopwords.words("english")
        tagged = nltk.pos_tag(stop_words)
        stop_words = stop_words[:30] + [x[0] for x in tagged[30:130] if not re.match('[JIR]', x[1])] + stop_words[130:] + ['s']
        result = [w for w in words if w not in stop_words]

        return ' '.join(result)

    def __preprocess(self, sentence):
        # Tokenize into words
        words = nltk.word_tokenize(sentence)

        # Remove non-alphnumeric characters
        words = [re.sub("^(?!')[\W_]+|(?!')[\W_]+$", '', i) for i in words]
        words = list(filter(None, words))

        # Empty sentence
        if not words:
            return []

        # Parts of Speech tagging
        tagged = nltk.pos_tag(words)

        # Chunk required group of words
        grammer = r'''Chunk: {<RB.?>+<VB.?>?(<DT>?<JJ.?>)+(<IN><PRP.?>?|<IN>?)(<DT>?<JJ.?>)*<NN.?>}
                             {<RB.?>+<VB.?>?(<DT>?<JJ.?>)*(<IN><PRP.?>?|<IN>?)(<DT>?<JJ.?>)+<NN.?>}
                             {<VB.?>?(<DT>?<JJ.?>)+(<IN><PRP.?>?|<IN>?)(<DT>?<JJ.?>)*<NN.?>}
                             {<VB.?>?(<DT>?<JJ.?>)*(<IN><PRP.?>?|<IN>?)(<DT>?<JJ.?>)+<NN.?>}
                             {<RB.?>+<VB.?>?(<DT>?<JJ.?>)*(<IN><PRP.?>?|<IN>?)(<DT>?<JJ.?>)+}
                             {<JJ.?>}'''
        chunker = nltk.RegexpParser(grammer)
        chunked = chunker.parse(tagged)
        chunks = [np.array(subtree) for subtree in chunked.subtrees() if subtree.label() == 'Chunk']

        return list(set(filter(None, [self.__process_chunk(chunk) for chunk in chunks])))

    def bag_of_words(self, review):
        # Tokenize into sentences
        sentences = nltk.sent_tokenize(review)
        return [x for sentence in sentences for x in self.__preprocess(sentence)]

    def __make_feature(self, word_list):
        return dict([(word, True) for word in word_list])

    # def __train_data(self, pos=None, neg=None):
    #     if pos == None:
    #         p = self.__pos
    #     else:
    #         p = pos
    #     if neg == None:
    #         n = self.__neg
    #     else:
    #         n = neg
    #     return [(self.__make_feature(self.bag_of_words(review)), 'positive') for review in p] + [(self.__make_feature(self.bag_of_words(review)), 'negative') for review in n]

    # def train(self, pos=None, neg=None, save=False):
    #     if pos == None and neg != None:
    #         raise Exception('pos is None and neg is not None')
    #     if pos != None and neg == None:
    #         raise Exception('pos is not None and neg is None')
    #     if pos != None and neg != None:
    #         if type(pos) != list and type(neg) != list:
    #             raise Exception('pos and neg aren\'t of type list')
    #         if len(pos) != len(neg):
    #             raise Exception('Unequal number of positive and negative reviews')

    #     # Train a data set
    #     self.__classifier = nltk.NaiveBayesClassifier.train(self.__train_data(pos, neg))

    #     if save:
    #         # Cache the features for faster predictions
    #         with open('classifier.pickle', 'wb') as f:
    #             pickle.dump(self.__classifier, f)


    def get_positive_data(self):
        return random.choice(self.__pos)

    def get_negative_data(self):
        return random.choice(self.__neg)

    # def predict(self, sentences):
    #     if type(sentences) is str:
    #         return self.__classifier.classify(self.__make_feature(self.bag_of_words(sentences)))
    #     else:
    #         return [self.__classifier.classify(self.__make_feature(self.bag_of_words(sentence))) for sentence in sentences]



    def main(self):
        # Train data sets
        # self.train(pos=self.__pos, neg=self.__neg, save=True)

        # Test data sets
        # print(self.predict(self.get_positive_data()))
        # print(self.predict(self.get_negative_data()))
        # print(self.predict(self.get_positive_data()))
        # print(self.predict(self.get_negative_data()))
        # print(self.predict(self.get_positive_data()))
        # print(self.predict(self.get_negative_data()))
        # print(self.predict(self.get_positive_data()))
        # print(self.predict(self.get_negative_data()))


        # pos = self.__pos[7]
        # print('\nPositive Review:\n', pos)
        # pos_words = self.bag_of_words(pos)
        # print('Filtered Words:\n', pos_words)
        # neg = self.__neg[39]
        # print('\nNegative Review:\n', neg)
        # print('Filtered Words:\n', self.bag_of_words(neg))
        # print('\nPrediction: ', self.predict([pos, neg]))


        with open('data.json') as data_file:
            datas = json.load(data_file)

        extracted_words = []
        for data in datas:
            dump = {
                'URL': data['URL']
            }
            reviews = data['REVIEW'].split(' \n ')
            dates = data['RDATE'].split(' \n ')
            if (len(reviews) > len(dates)):
                reviews = reviews[len(reviews)-len(dates):]

            bags = collections.defaultdict(list)
            for i, review in enumerate(reviews):
                words = self.bag_of_words(review)
                words = ', '.join(map(str, words))
                # bags[i] = words
                rev = {
                    'REVIEW': words,
                    'DATE': dates[i]
                }
                bags[i] = rev
            dump['REVIEWS'] = bags
            extracted_words.append(dump)
            
        with open('bag_of_words.json', 'w') as f:
            json.dump(extracted_words, f, indent=4)


        # print(self.predict(self.__pos[:5] + self.__neg[:5]))

        # for i in range(1):
        #     print(i, self.bag_of_words(self.__pos[i]))
        # for i in range(10, 20):
        #     print(i, self.bag_of_words(self.__neg[i]))

        # print(self.bag_of_words('not that bad'))
        # print(self.bag_of_words('very bad'))
        # print(self.bag_of_words('not very bad'))
        # print(self.bag_of_words('boring'))


if __name__ == '__main__':
    myObj = Sentiment()
    myObj.main()