#!/usr/bin/python

import string
import sys


sys.path.append("tools/")
from named_entity import getNamedEntities

def checkNamedEntities(text):

    word_data = text.translate(string.maketrans("", ""), string.punctuation)
    
    names = getNamedEntities(text)
    dic = {}
    #all_words = []
    words = text.split()
    #print words
    #for x in words:
        #x = x.decode("utf8", 'ignore')
        #all_words.append(x)
    for word in words:
        if word in names:
            dic.update({word: 1})
        else:
            dic.update({word: 0})
    return dic


