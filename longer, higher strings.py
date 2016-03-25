def long_high_word(wordlist):
    if wordlist == []:
        return False
    else:
        max = 0
        len_list = []
        for i in range(0, len(wordlist)):
            count = len(wordlist[i])
            len_list.append(count)
        
        len_list.sort(reverse=True)
        
        maxn = len_list[0]         
        max_string = []
        for i in range(0, len(wordlist)):
            if len(wordlist[i])==maxn:
                max_string.append(wordlist[i])
        max_string.sort(reverse = True)
        return max_string[0]
                    
                        

                