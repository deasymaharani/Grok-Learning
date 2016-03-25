def prevword_ave_len(word):
    text = "Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off - then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
    for item in text:
        word_list = text.split(' ')
    if not word in word_list:
        return False
    else:
        word_prev = []
        len_prev = 0
        if word == word_list[0]:
                len_prev = 0
                word_prev.append(len_prev)  
        for i in range (1,len(word_list)):
            if word_list[i] == word:
                word_prev.append(len(word_list[i-1]))
        sumlen = 0
        for i in range (0,len(word_prev)):
            sumlen = sumlen + word_prev[i]
        average_length = sumlen/len(word_prev)
        return average_length