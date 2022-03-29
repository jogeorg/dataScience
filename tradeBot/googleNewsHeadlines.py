# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:19:31 2022

@author: jogeorg
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import CountVectorizer

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
headlines=" ".join(str(elem) for elem in headlines)

# Vectorize headlines
#countvector=CountVectorizer(ngram_range=(2,2))
#traindataset=countvector.fit_transform(headlines)

# Add to csv file
#df = pd.DataFrame(header=)
#df.loc[len(df)] = headlines
#df.to_csv('output.csv', columns = header)
