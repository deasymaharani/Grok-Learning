def sorted_words(wordlist):
    sortedlist = []
    returnlist = []
    for i in range (0,len(wordlist)):
        sortedlist.append(sorted(wordlist[i]))

    wordfix=[]
    word = ''
    for i in range (0, len(sortedlist)):
        for j in range (0, len(sortedlist[i])):
            word = word+sortedlist[i][j]
        wordfix.append(word)
        word = ''
 
    for i in range(len(wordfix)):
        if wordfix[i] == wordlist[i]:
            returnlist.append(wordfix[i])
 
    returnlist.sort()
    
    return returnlist
        