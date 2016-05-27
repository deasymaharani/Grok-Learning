def longest_sentence_length(text):
    sent_list = text.split('.')
    count = []
    for item in sent_list:
        if item != '':
            item = item.strip()
            word_list = item.split(' ')
            count.append(len(word_list))
    if count != []:
        count.sort(reverse=True)
        return count[0]
    else: 
        return 0