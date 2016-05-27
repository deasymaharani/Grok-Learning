def symmetric_words(wlist):
    
    #create function to check the symmetricity
    def is_symmetric(word):
        if len(word)%2 == 1:
            return False
        for i in range(0,len(word)//2):
            if ord(word[i]) - ord('a') != ord('z') - ord(word[-(i+1)]):
                return False
        return True
    #obtain the sorted list of symmetric words
    newlist = sorted([w for w in wlist if is_symmetric(w)])
    return newlist