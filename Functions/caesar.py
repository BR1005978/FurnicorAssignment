

def encrypt(text,s = 8):
    encryption = ""
    for c in text:
        encryption += chr(ord(c) + s)
    return encryption

def decrypt(text,s = 8):
    encryption = ""
    for c in text:
        encryption += chr(ord(c) - s)
    return encryption

#check the above function
# text = "CEASER CIPHER DEMO12345678"
# text = "A 5 "
s = 8