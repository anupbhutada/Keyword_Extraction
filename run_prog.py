import os
import numpy
import string
import math
import string
import files_read
import wordpositionlist
import count_vectorize
import check_named_entity
import check_noun_phrase
import wordpositionlist
import distbetwords
import get_word_length
import tfidf
import capitalisation
import wikifreq
import finalkeywords
import pred_keywords
from time import time
import pickle

adds = files_read.add_read("C:\\Users\\ANUP\\Documents\\machine_learning\\datasets\\500N-KPCrowd-v1.1\\CorpusAndCrowdsourcingAnnotations\\train")

#all_text = ["my name is Anup it is", "is I Divyansh Goel in an working ass hole ass Divyansh", "is this working right this"]
all_cont = files_read.read_all(adds)
#print all_cont
print "--------------------------------------"
all_text = files_read.remove_punct(all_cont)
#print all_text
p = ["""Hope you are all set for PS -I program that is commencing from Monday.
Ms. Ekta will be contact person from Keval and Mr. Prakrash,  PS Student co-instructor will also be available there. You are expected to reach by 10.45 am and report to Ekta, HR manager. 
Chief HR manager will address you and will discuss about program. They are finalizing projects and expected deliverables. 
Do some homework about company and ask intelligent questions.
Working days will be from Monday to Friday and working hours will be 9-6 pm.
I will be busy in commencing program at other stations on Monday, so will meet you all on Tuesday.
Feel free to take help from Prakrash as he is quite senior to you with industry experience. Make sure you reach on time and be in formals.
Always remember you are brand ambassador of BITS, so lot of responsibilities lie on your shoulders. Your batch will be the first PS batch at Keva, so their expectations are quite high and I am fully confident that you meet them.
Prakrash is available at 8779683930.
All The Best!
Feel free to call me in any difficulty/clarification.
"""]
comb_text = all_text + files_read.remove_punct(p)
with open('comb_text.pkl', 'wb') as fl:
	pickle.dump(comb_text, fl)

dic_arr = files_read.id_words(all_text)
#print dic_arr
comb_dic_arr = files_read.id_words(comb_text)

def flipIdDic(id_dic_arr):
	idtowords_dic = {}
	for dic in id_dic_arr:
		flipped_dic = dict((v,k) for k,v in dic.iteritems())
		idtowords_dic.update(flipped_dic)
	return idtowords_dic
idtowords = flipIdDic(dic_arr)
#print idtowords
#print files_read.feat_arr(wordpositionlist.wordpos, all_text, dic_arr)


#score_dic = [count_vectorize.term_freq(text) for text in all_text]
termfreq_arr = count_vectorize.feat_arr(count_vectorize.term_freq, all_text, dic_arr)
#print score_dic
#print termfreq_arr

#nameentity_dic = [check_named_entity.checkNamedEntities(text) for text in all_text]
nameentity_arr = files_read.feat_arr(check_named_entity.checkNamedEntities, all_text, dic_arr)
#print nameentity_arr

#nounphrase_dic = [check_noun_phrase.checkNounPhrases(text) for text in all_text]
nounphrase_arr = files_read.feat_arr(check_noun_phrase.checkNounPhrases, all_text, dic_arr)
#print nounphrase_dic
#print nounphrase_arr

#wordpos_dic = [wordpositionlist.wordpos(text) for text in all_text]
wordpos_arr = files_read.feat_arr(wordpositionlist.wordpos, all_text, dic_arr)
#print wordpos_dic
#print wordpos_arr

#distrms_dic = [distbetwords.disBetWords(text) for text in all_text]
distrms_arr = files_read.feat_arr(distbetwords.disBetWords, all_text, dic_arr)
#print distrms_dic
#print distrms_arr

#wordlen_dic = [get_word_length.getWordLength(text) for text in all_text]
wordlen_arr = files_read.feat_arr(get_word_length.getWordLength, all_text, dic_arr)
#print wordlen_dic
#print wordlen_arr

#tfidf_dic = tfidf.tfidFreq(all_text) 		#not like all others !special attention req
tfidf_arr = tfidf.tfidf_arr(all_text, dic_arr)   #comb_text is a combined array of training and pred texts
with open('tfidf_arr.pkl', 'wb') as fl:
	pickle.dump(tfidf_arr, fl)
#print tfidf_dic
#print tfidf_arr

#caps_dic = [capitalisation.capitalWords(text) for text in all_text]
caps_arr = files_read.feat_arr(capitalisation.capitalWords, all_text, dic_arr)
#print caps_dic
#print caps_arr

#wiki_dic = [wikifreq.wikifrequncy(text) for text in all_text]
wiki_arr = files_read.feat_arr(wikifreq.wikifrequncy, all_text, dic_arr)
#print wiki_dic
#print wiki_arr
print len(termfreq_arr)

#features = files_read.featfromarr(termfreq_arr, tfidf_arr, nameentity_arr, nounphrase_arr, wordpos_arr, distrms_arr, wordlen_arr, caps_arr, wiki_arr)
with open('extracted_feat1.pkl', 'rb') as fil:
	features = pickle.load(fil)
#print features
print "features created"

from sklearn import preprocessing
features_arr = numpy.asarray(features)

global min_max_scaler
min_max_scaler = preprocessing.MinMaxScaler()
features_norm = min_max_scaler.fit_transform(features_arr)
with open('min_max_scaler.pkl', 'wb') as fl:
	pickle.dump(min_max_scaler, fl)
#print features_norm
train_len = len(features)
print 'feat len:', train_len
with open('train_len.pkl', 'wb') as fl:
	pickle.dump(train_len, fl)

keywords = files_read.getkeywords("C:\\Users\\ANUP\\Documents\\machine_learning\\datasets\\500N-KPCrowd-v1.1\\CorpusAndCrowdsourcingAnnotations\\train")
#print keywords
labels = finalkeywords.getlabels(keywords, dic_arr)
print "labelled"

#features_train = features_norm
#labels_train = labels


def splitData(features, labels):
	f_train = []
	l_train = []
	for x in range(len(features)):
		f_train.append(features[x])
		l_train.append(labels[x])
	return f_train, l_train


#from sklearn.model_selection import train_test_split
f_train, l_train = splitData(features_norm, labels)
#print f_train.shape
print len(f_train), len(l_train)
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=50)

#from sklearn.ensemble import AdaBoostClassifier
#clf = AdaBoostClassifier(n_estimators=10)

#from sklearn.svm import SVC
#clf = SVC(kernel = 'rbf', C = 10000, gamma = 10)

t0 = time()
clf.fit(f_train, l_train)
print "training time:", round(time()-t0, 3), "s"
with open('classifier.pkl', 'wb') as fl:
	pickle.dump(clf, fl)
'''
t1 = time()
pred = clf.predict(f_test)
print "prediction time:", round(time()-t1, 3), "s"

print

n=len(pred)
pred_keywords = []
for i in range(n):
	if pred[i]==1:
		pred_keywords.append(idtowords[i+splitting_index])
print pred_keywords

reord_keywords = files_read.reorderkeywords(pred_keywords, wordpos_arr, dic_arr)
for x in reord_keywords:
	print x

print "*************predicted******************"

#from sklearn.metrics import accuracy_score
#print "accuracy:",accuracy_score(l_test, pred)
'''
import pred_keywords
pred_keywords.extKeywords(p)
