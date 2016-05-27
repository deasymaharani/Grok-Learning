def maxby(intlist):
    if not intlist:
        return(None, None)
    elif len(intlist)==1:
        return(intlist[0], None)
    else:
        sortedlist = sorted(intlist, reverse=True)
        maxnum = sortedlist[0]
        bymargin = sortedlist[0] - sortedlist[1]
        return(maxnum, bymargin)
        
    