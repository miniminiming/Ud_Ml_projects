
import os
import pickle
import re
import sys

print "loading processed emails"
word_data = pickle.load(open("your_word_data.pkl", "r") )
from_data = pickle.load(open("your_email_authors.pkl", "r") )

print("word_data[152] is: %s" % word_data[152])

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit_transform(word_data)

print("vocabulary size is: %d" % len(vectorizer.vocabulary_))
print("word number 34597 is: %s" % vectorizer.get_feature_names()[34597])