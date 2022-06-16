

def encrypt(text,s = 8):
    encryption = ""
    for c in text:
        encryption += chr(ord(c) + s)

    print(f"[DEV] encrypted string: {encryption}")
    return encryption

def decrypt(text,s = 8):
    decryption = ""
    for c in text:
        decryption += chr(ord(c) - s)

    print(f"[DEV] decrypted string: {decryption}")
    return decryption

#check the above function
# text = "CEASER CIPHER DEMO12345678"
# text = "A 5 "
s = 8