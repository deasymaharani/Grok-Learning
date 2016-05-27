def validate_card(cardnum):
    if not cardnum.isdigit() or len(cardnum) != 16:
        return False
    else:
        sum = 0
        for item in cardnum:
            sum = sum + int(item)
        if sum % 10 == 0:
            return True
        else:
            return False    

        