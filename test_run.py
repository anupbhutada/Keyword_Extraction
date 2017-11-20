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
from time import time
import pickle

adds = files_read.add_read("C:\\Users\\ANUP\\Documents\\machine_learning\\datasets\\500N-KPCrowd-v1.1\\CorpusAndCrowdsourcingAnnotations\\small")

#all_text = ["my name is Anup it is", "is I Divyansh Goel in an working ass hole ass Divyansh", "is this working right this"]
all_cont = files_read.read_all(adds)
#print all_cont
print "--------------------------------------"
all_text = files_read.remove_punct(all_cont)
#print all_text
dic_arr = files_read.id_words(all_text)
#print dic_arr
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
tfidf_arr = tfidf.tfidf_arr(all_text, dic_arr)
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
def idforsplitting(altext, arr1):
	idforlastmail = len(arr1)
	#print idforlastmail
	for x in arr1:
		if x[0] == len(altext)-1:
			if x[1]<idforlastmail:
				idforlastmail = x[1]
	return idforlastmail

splitting_index = idforsplitting(all_text, wiki_arr)
print "splitting Index:", splitting_index
features = files_read.featfromarr(termfreq_arr, tfidf_arr, nameentity_arr, nounphrase_arr, wordpos_arr, distrms_arr, wordlen_arr, caps_arr, wiki_arr)
#with open('extracted_feat.pkl', 'rb') as fil:
#	features = pickle.load(fil)
#print features
print "features created"

from sklearn import preprocessing
features_arr = numpy.asarray(features)

min_max_scaler = preprocessing.MinMaxScaler()
features_norm = min_max_scaler.fit_transform(features_arr)
#print features_norm

keywords = files_read.getkeywords("C:\\Users\\ANUP\\Documents\\machine_learning\\datasets\\500N-KPCrowd-v1.1\\CorpusAndCrowdsourcingAnnotations\\small")
#print keywords
labels = finalkeywords.getlabels(keywords, dic_arr)
print "labelled"

#features_train = features_norm
#labels_train = labels


def splitData(features, labels, splitting_index):
	f_train = []
	l_train = []
	f_test = []
	l_test = []
	for x in range(splitting_index):
		f_train.append(features[x])
		l_train.append(labels[x])
	for x in range(splitting_index, len(features)):
		f_test.append(features[x])
		l_test.append(labels[x])
	return f_train, f_test, l_train, l_test


#from sklearn.model_selection import train_test_split
f_train, f_test, l_train, l_test = splitData(features_norm, labels, splitting_index)
#print f_train.shape
print len(f_train), len(f_test), len(l_train), len(l_test)
print f_test
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()

from sklearn.svm import SVC
clf = SVC(kernel = 'rbf', C = 100, gamma = 10)

t0 = time()
clf.fit(f_train, l_train)
print "training time:", round(time()-t0, 3), "s"

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
