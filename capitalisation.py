#find the capital words 
# feature= capital word value s 1 otherwise value is 0

def findcap(word) :
    for i in word :
        if i.isupper() == True :
            bool = True
            break
        else :
            bool = False
        #print "for word:",word,"and i",i,"bool is",bool
    return bool

def capitalWords(file) :
    list = file.split()
    dict = {}
    i = 0
    while i<len(list) :
        index = i
        word = list[i]
        if not word in dict :
            dict[word]=0
            bool=findcap(word)
            #print "for word bool= ",word," ",bool
            if bool == True :
                dict[word]=1
        i = i+1
    return dict