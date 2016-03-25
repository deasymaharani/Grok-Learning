import operator
def top5_words(text):
    wordlist = text.split()    
    dict_count = {}   
    for word in wordlist:
        if word in dict_count:
            dict_count[word] = dict_count[word] + 1
        else:
            dict_count[word] = 1
    sort_dic = sorted(dict_count.items(), key=operator.itemgetter(1), reverse=True)
    sort_dic = [(t[1], t[0]) for t in sort_dic]
    #print(sort_dic)
    temp=[]
    result = []
    i=0
    while i < len(sort_dic):
        temp = []
        temp = [w for f, w in sort_dic if f==sort_dic[i][0]]
        temp = sorted(temp)
        result = result + temp
        i = i+len(temp)   
    if len(result) > 5:
        result = result[0:5]
        #print(result)    
        return result
    else:
        return result   