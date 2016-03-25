def middle_words(word_list):
    mdl_word=[]
    if len(word_list) % 2 == 0:
        idx = int(len(word_list)/2) 
        mdl_word.append(word_list[idx-1])
        mdl_word.append(word_list[idx])
    else:
        idx = int(len(word_list)/2)
        mdl_word.append(word_list[idx])
    return mdl_word