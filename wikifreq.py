#get the wikipedia freq for words in a text
import wikiwords

def wikifrequncy(file) :
    list = file.split()
    dict = {}
    for i in range(len(list)) :
        word = list[i]
        if not word in dict :
            dict[word] = wikiwords.freq(word)
    return dict