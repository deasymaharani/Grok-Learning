def repeat_word_count(text, n):
    wordlist = text.split()    
    dict_count = {}   
    for word in wordlist:
        if word in dict_count:
            dict_count[word] = dict_count[word] + 1
        else:
            dict_count[word] = 1
    
    word_great = []
    for word in dict_count:
        if dict_count[word] >= n:
            word_great.append(word)
    word_great.sort()
    
    return word_great
        