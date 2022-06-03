# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:19:31 2022

@author: jogeorg
"""
# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

# -------------------------------------------------------------------#

# Get learned
train=pd.read_csv('Kaggle/Combined_News_DJIA.csv', encoding = "ISO-8859-1")

# Removing punctuations
data=train.iloc[:,2:27]
data.replace("[^a-zA-Z]"," ",regex=True, inplace=True)

# Renaming column names for ease of access
list1= [i for i in range(25)]
new_Index=[str(i) for i in list1]
data.columns= new_Index
data.head(5)

# Convertng headlines to lower case
for index in new_Index:
    data[index]=data[index].str.lower()
data.head(1)

' '.join(str(x) for x in data.iloc[1,0:25])

headlines = []
for row in range(0,len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row,0:25]))
    
headlines[0]

# BoW
countvector=CountVectorizer(ngram_range=(2,2))
traindataset=countvector.fit_transform(headlines)

# 0-1 sparse matrix
traindataset[0]

# implement RandomForest Classifier
randomclassifier=RandomForestClassifier(n_estimators=400,criterion='entropy')
randomclassifier.fit(traindataset,train['Label'])

# -------------------------------------------------------------------#

# Get webpage request
url = 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'
page = requests.get(url)

# Set local variables for later calls
soup = BeautifulSoup(page.content, 'html.parser')
headlines = soup.find_all('a', text=True)
list = []

# Scrape the webpage for news headlines
for headline in headlines:
    headline = re.sub('[^a-zA-Z0-9]'," ",headline.text.lower())
    list.append(headline)
headlines = list[3:-3:2]
test_dataset = countvector.transform(headlines)
predictions = randomclassifier.predict(test_dataset)

# Predictions
randomclassifier.predict(test_dataset)