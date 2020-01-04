import pandas as pd
import numpy as np
import csv
import string
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer

#Select the reviews and the ratings from the dataset
data = pd.DataFrame()
data = pd.read_csv('customerreviews.csv', encoding='utf-8')
reviews = data.loc[:,'Reviews'].values
ratings = data.loc[:,'Ratings'].values

#Avoid punctuations
punctuationsRemoved = []
punctuations = '''!()-[]{};:",<>./?@#$%^&*_~'''
for i in reviews:
    punctuationsRemoved.append(i.translate(str.maketrans
    ('', '', string.punctuation)).lower())

#Stopword Removal and change everything to thelowerCase
grammarErrorFree = []
grammar = ['the','an','ve','between','onto','is','into','who',
'with','and','he','she','for','up','you','when','where','me',
'in','of','as','at','from','my','was','i','am','a','to','were',
'are','this','it','that','those','so','or','which','has','have','had',
'whom','if','whether','isnt','ive','a','b','c','d','e','f','g','h','i',
'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for iterate in punctuationsRemoved:
    x = [i for i in iterate.split()]
    string = ""
    for k in x:
        k = k.lower()
        if k not in grammar:
            string = string +" "+ k
    grammarErrorFree.append(string)

# #Avoid numbers in the reviews
avoid_numbers = []
for a in grammarErrorFree:
    avoid_numbers.append(''.join([i for i in a if not i.isdigit()]))

#Avoid shortwords
wordbag = []
for i in avoid_numbers:
    lengthOfWords = i.split(" ")
    lengthOfWords = ' '.join([i for i in lengthOfWords if len(i)>=3])
    wordbag.append(lengthOfWords)

#Stemming
resultantWordBag = []
ps = PorterStemmer()
for i in wordbag:
    string = ""
    for j in i:
        string = ps.stem(j) + " "
    resultantWordBag.append(string)

resultantWordBag = wordbag

#Vectorization using TF-IDF
vectorizer = TfidfVectorizer(min_df = 5,
                             max_df = 0.8,
                             ngram = (1,2),
                             sublinear_tf = True,
                             use_idf = True)
train_vectors = vectorizer.fit_transform(resultantWordBag)


# Perform classification with SVM, kernel=linear
classifier_linear = svm.SVC(kernel='linear')

# Training the model from the dataset taken from kaggle
classifier_linear.fit(train_vectors, ratings)

# Read each individual file -> Here the customer reviews
#are scraped from the internet using Scrapy python.
fileList = []
predictionList = []
fileList.append('acerAspire.csv')
fileList.append('appleMacbookAir.csv')
fileList.append('appleMacbookPro.csv')
fileList.append('asusChrome.csv')
fileList.append('dellXps.csv')
fileList.append('lenovoIdeaPad.csv')
fileList.append('microsoftSurface.csv')
predictionList.append('acerAspirePrediction.csv')
predictionList.append('appleMacbookAirPrediction.csv')
predictionList.append('appleMacbookProPrediction.csv')
predictionList.append('asusChromePrediction.csv')
predictionList.append('dellXpsPrediction.csv')
predictionList.append('lenovoIdeaPadPrediction.csv')
predictionList.append('microsoftSurfacePrediction.csv')

for i in range(0,len(fileList)):
    reviewsFetch =pd.read_csv(fileList[i], encoding='utf-8')
    comments = reviewsFetch.loc[:,'comment'].values
    listnew = []
    listnew.append("Review")
    listnew.append("Sentiments")
    with open(predictionList[i], mode = 'w') as csvFile:
        reviewWrite = csv.writer(csvFile, delimiter=',')
        reviewWrite.writerow(listnew)
        for iterate in comments:
            review = iterate
            predict = []
            review_vector = vectorizer.transform([review]) # vectorizing
            predict.append(review)
            predict.append(classifier_linear.predict(review_vector))
            reviewWrite.writerow(predict)
