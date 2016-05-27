def make_gamertag(name):
    result = ""
    for item in name:
        result = result + item + "*"
    return result 
