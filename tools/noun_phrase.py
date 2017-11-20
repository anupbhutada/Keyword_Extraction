#!/usr/bin/python

import nltk

    
def nounPhrase(t):
    
    text = t
    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    grammar = r"""
    NP:
    {<NN.*|JJ>*<NN.*>}
    """
    cp = nltk.RegexpParser(grammar)
    tagged_sent = [cp.parse(sent) for sent in sentences]

    return tagged_sent


def getNounPhrases(text):
    
    np_tagged = nounPhrase(text)
    #print np_tagged[90]

    noun_phrases = []
    for sent in np_tagged:
        for x in sent:         
            if type(x) is nltk.tree.Tree:
                if x.label() == 'NP':
                    noun_phrases.append(x)
    cleaned = []
    for tree in noun_phrases:
        for leaf in tree.leaves():
            cleaned.append(leaf[0])
    
    return cleaned 

#print getNamedPhrases(p)




