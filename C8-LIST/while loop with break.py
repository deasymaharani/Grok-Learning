def wordlist(text):
    alphalist=[]
    if text == '':
        return alphalist
    else:
        words = text.split(' ')
        i = 0
        alphalist=[]
        while i < len(words):
            if words[i].isalpha():
                alphalist.append(words[i])
                i = i+1
            else:
                break
    return alphalist