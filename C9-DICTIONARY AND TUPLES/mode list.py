def mode(numlist):
    dic_num = {}
    if numlist == '':
        return 0
    else:
        for item in numlist:
            if item in dic_num:
                dic_num[item] = dic_num[item]+1
            else:
                dic_num[item] = 1    
    
    maxn = max(dic_num.values())
    newlist = []
    for item in dic_num:
        if dic_num[item] == maxn:
            newlist.append(item)
    newlist.sort()
    return newlist