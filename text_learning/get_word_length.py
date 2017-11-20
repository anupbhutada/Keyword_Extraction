#!/usr/bin/python

import os

def getWordLength(f):

    f.seek(0)
    t = f.read()
    word_length = {}
    if len(t) > 1:
        dic = eval(t)
        for key, value in dic.items():
            strlen = len(key)
            word_length.update({key: strlen})
    
    return word_length

    

def main():
    ff = open("vocabulary.txt", "r")
    len_dict = getWordLength(ff)
    ff.close()
    ff = open("word_length.txt", "w")
    ff.write(str(len_dict))
    ff.close()
    print "File Ready"



if __name__ == '__main__':
    main()

