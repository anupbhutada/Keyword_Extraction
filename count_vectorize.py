#!/usr/bin/python

def term_freq(text):

    word_data = [text]
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(min_df=0, encoding="utf-8", token_pattern='\\b\\w+\\b', lowercase=False)
    bag = vectorizer.fit_transform(word_data)
    feature_names = vectorizer.get_feature_names()
    doc = 0
    feature_index = bag[doc,:].nonzero()[1]
    freq = zip(feature_index, [bag[doc, x] for x in feature_index])

    score_dic = {}

    for w, s in [(feature_names[i], s) for (i, s) in freq]:
        score_dic.update({w: s})

    return score_dic



def feat_arr(function, mails, arrK) :               #mails is list of mails(string), arrk is array of dict of every mail
    mailNo=0
    listO = []
    for mail in mails :
        dict = function(mail)
        dict1 = arrK[mailNo]
            
        for key in dict1.keys() :
            iden = dict1[key]
            list1 = [mailNo, iden, dict[key]]
            listO.append(list1)
        mailNo = mailNo+1
    return listO