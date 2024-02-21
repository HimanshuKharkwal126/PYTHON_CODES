
str=input("enter the password:")
uc=s=d=l=sc=d=0
for i in str:
    if i.isupper():
        uc+=1
    if i.isspace():
        s+=1
    if i in ["@","#","$","~","&"]:
        sc+=1
    if i.isdigit():
        d+=1
if len(str)>8 and uc>=1 and s==0 and sc>=1 and d>=1:
    print("Valid password:")
else:
    print("Invalid password:")
    
    
    
    
    # using while loop
    

c=False
while(c==False):
    str=input("enter the Password:")
    uc=s=d=l=sc=0
    for i in str:
        if i.isupper():
            uc+=1
        if i.isspace():
            s+=1
        if i in["@","#","$","&","~"]:
                sc+=1
    if len(str)>8 and uc>=1 and s==0 and sc>=1:
        print("Valid Password")
        c=True
    else:
        print("Invalid Password")
        c=False
