def encrypt_message(text,x):
    encrypt_item=""
    for item in text:
        shift = ord(item)+x
        encrypt = chr(shift)
        encrypt_item = encrypt_item+encrypt
    return encrypt_item
