def kinda_fermat(a,b,c):
    #check var a,b,c if integer 
    if not isinstance(a,int) or not isinstance(b,int) or not isinstance(c,int):
        return False
    #if it's integer, calculate the function
    else:
        nlist=[]
        n = list(range(2,11))
        for i in n:
            if a**i + b**i == c**i:
                nlist.append(i)
        if nlist == []:
            return False
        else:
            return nlist[0]
        