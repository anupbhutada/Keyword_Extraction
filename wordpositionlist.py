# word position-1st position

def wordpos(file) :
    list = file.split()
    dict = {}

    for i in range(len(list)) :
        word = list[i]
        if not word in dict :
            dict[word] = i+1
    return dict

def fun(function, mails, arrK) :               #mails is list of mails(string), arrk is array of dict of every mail
    mailNo=0
    listO = []
    for mail in mails :
        file = mail.split()
        dict = function(mail)
        for key in dict.keys() :
            dict1 = arrK[mailNo]
            iden = dict1[key]
            list1 = [mailNo, iden, dict[key]]
            listO.append(list1)
        mailNo = mailNo+1
    return listO             