def encrypt(str,key):
    return key.join(str)
def decrypt(str,key):
    return str.split(key)
mainstr=input("enter the main string:")
encryptstr=input("enter encrypted string:")
enstr=encrypt(mainstr,encryptstr)
deLst=decrypt(mainstr,encryptstr)
destr="".join(deLst)
print(enstr)
print(destr)
