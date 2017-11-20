import math
import string

def addword(dict,word) :
    if not word in dict :
        dict[word] = []
        
def finddistance(word,index,list) :
    try :
        next = list.index(word,index+1)
      # print "next element at: ",next
        return next-index
    except :
        return 0

def adddistance(distance,dict,word) :
    l = dict[word]
    if distance != 0 :
        l.append(distance)

f = open("test.txt","r")
content = f.read()
file = content.translate(string.maketrans("", ""), string.punctuation)
file = ''.join([c for c in file if c not in ('!', '?' )])  # this line removes punctuation , add punctuations in the bracket 
list = file.split()
f.close()
# print "list is: ",list
dict = {}

i = 0

while i<len(list) :
  # print "for the word :",word
    index = i
    word = list[i]
 #  print "index is: ",index
    addword(dict,word)
 #  print "after adding to dict:",dict
    distance = finddistance(word,index,list)
 #  print "distance bw words: ",distance
    adddistance(distance,dict,word)
#   print "after loop dict: ",dict
    i = i+1

#print dict

rms_list = []

for key, value in dict.items():
    sm = 0.0
    for x in value:
        sm = sm + math.pow(x, 2)
    if len(value) != 0:
        rms = math.sqrt(sm/len(value))
    if len(value) == 0:
        rms = 0
    rms_list.append(rms)

rms_dict = {word: rms for word, rms in zip(dict.keys(), rms_list)}


f = open("dist_rms.txt", "w")
f.write(str(rms_dict))
f.close()



    
