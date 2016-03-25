def unique_long_words(wlist,wlen):
    unique = []
    
    #create list of unique words
    for i in range (0,len(wlist)):
        if wlist[i] in unique:
            continue
        else:
            unique.append(wlist[i])
    
    #obtain words which length is greater than or eq to wlen
    unique_great = [w for w in unique if len(w)>=wlen]
    return len(unique_great)
       