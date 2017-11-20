#!/usr/bin/python

import string
import sys


sys.path.append("tools/")
from noun_phrase import getNounPhrases

def checkNounPhrases(text):

    word_data = text.translate(string.maketrans("", ""), string.punctuation)
    nouns = getNounPhrases(text)

    dic = {}
    all_words = []
    words = text.split()
    #for x in words:
        #x = x.decode("utf8", 'ignore')
        #all_words.append(x)
    for word in words:
        if word in nouns:
            dic.update({word: 1})
        else:
            dic.update({word: 0})
    
    return dic
    
