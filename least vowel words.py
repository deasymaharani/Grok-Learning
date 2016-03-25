import operator
def least_vowel_words(text):
    unique = []
    wordlist=[]
    wordlist = text.split()
    #print(wordlist)
    for item in wordlist:
        if item in unique:
            continue
        else:
            item = item.rstrip(',.:;!?-\'\"')
            if item != '':
                unique.append(item.lower())
    dic = {}
    for i in range(0, len(unique)):
        count = 0
        for char in unique[i]:
            if char in ('a','i','u','e','o'):
                count = count + 1
        prop = float(count)/float(len(unique[i]))
        dic[unique[i]] = prop
    sort_dic = sorted(dic.items(), key=operator.itemgetter(1))
    #print(sort_dic)
    result = [k for k,v in sort_dic if v==sort_dic[0][1]]
    #print(result)    
    newlist=[]
    for word in unique:
        if word in result:
            newlist.append(word)
    #print(newlist)
    return newlist        
            
            
            
    