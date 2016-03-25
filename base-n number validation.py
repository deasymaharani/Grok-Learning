def basenum(num, base):
    numstr = str(num)
    for num in numstr:
        if int(num) > 0 or base<10: 
            for item in numstr:
                if int(item) >= base:
                    return False
            return True 
        else:
            return True    