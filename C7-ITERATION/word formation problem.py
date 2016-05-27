def word_suffix(initial, suff):    
    for letter in initial:
        print(letter+suff)
    return
    

initial = input("Enter the initial letters: ")
suff = input("Enter the common suffix: ")

word_suffix(initial, suff)
