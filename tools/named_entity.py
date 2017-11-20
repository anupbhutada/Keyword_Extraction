#!/usr/bin/python

import sys
import nltk


def getNamedEntities(text):
    
    def nameEntity(t):

        text = t
        
        sentences = nltk.sent_tokenize(text.decode("utf8", 'ignore'))
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        tagged_sent = [nltk.ne_chunk(sent, binary=True) for sent in sentences]

        return tagged_sent



    ne_tagged = nameEntity(text)
    #print ne_tagged[0]

    named_entity = []
    for sent in ne_tagged:
        for x in sent:         
            if type(x) is nltk.tree.Tree:
                if x.label() == 'NE':
                    named_entity.append(x)
    cleaned = []
    for tree in named_entity:
        for leaf in tree.leaves():
            cleaned.append(leaf[0])
    
    return cleaned




