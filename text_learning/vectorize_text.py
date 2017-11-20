#!/usr/bin/python

import os
import pickle
import re
import sys
import numpy as np

np.set_printoptions(threshold=np.nan)
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


f_list  = open("..\\add1.txt", "r")


from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0
n = 0


for path in f_list:
    ### only look at first 200 emails when developing
    ### once everything is working, remove this line to run over full dataset
    
    if temp_counter < 100:
            temp_counter += 1
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")
                
            ### use parseOutText to extract the text from the opened email
            parsed_email = parseOutText(email)
            
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            #words_to_remove = ["sara", "shackleton", "chris", "germani"]
            #print parsed_email
            #for word in words_to_remove:
            #    parsed_email = parsed_email.replace(word+' ', "")
            #print parsed_email
            ### append the text to word_data
            word_data.append(parsed_email)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
                  
            n += 1

            email.close()
        
            #print "Email not found"
print n, "emails processed"
f_list.close()


pickle.dump( word_data, open("mails_cont.pkl", "w") )



#print word_data

### in Part 4, do TfIdf vectorization here

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(word_data)
feature_names = vectorizer.get_feature_names()
doc = 0
feature_index = tfidf_matrix[doc,:].nonzero()[1]
tfidf_scores = zip(feature_index, [tfidf_matrix[doc, x] for x in feature_index])

score_dic = {}

for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
    score_dic.update({w: s})

fil = open("tfidf_score.txt", 'w')
fil.write(str(score_dic))
fil.close()

print "File Ready"

