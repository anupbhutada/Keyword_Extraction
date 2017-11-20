#!/usr/bin/python

import os
import pickle
import re
import sys
import numpy as np

np.set_printoptions(threshold=np.nan)
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

def tfidFreq(all_text_prepro, comb_text):

    word_data = all_text_prepro

    #print word_data

    ### in Part 4, do TfIdf vectorization here

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(min_df=0, token_pattern='\\b\\w+\\b', lowercase=False)
    vectorizer.fit(comb_text)
    tfidf_matrix = vectorizer.transform(word_data)
    #print tfidf_matrix
    feature_names = vectorizer.get_feature_names()
    score_dic = {}
    doc = 0
    for doc in range(len(word_data)): 
        
        feature_index = tfidf_matrix[doc,:].nonzero()[1]

        tfidf_scores = zip(feature_index, [tfidf_matrix[doc, x] for x in feature_index])    
        
        for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
            score_dic.update({w: s})
        doc = doc + 1
    #print score_dic
    return score_dic


def tfidf_arr(mails, arrK, comb_text) :               #mails is list of mails(string), arrk is array of dict of every mail
    mailNo=0
    listO = []
    dict = tfidFreq(mails, comb_text)
    for mail in mails :
        
        dict1 = arrK[mailNo]
        for key in dict1.keys() :
            iden = dict1[key]
            list1 = [mailNo, iden, dict[key]]
            listO.append(list1)
        mailNo = mailNo+1
    return listO 