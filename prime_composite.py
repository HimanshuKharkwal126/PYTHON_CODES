n=int(input("enter the number:"))
count=0
for i in range(1,n+1):
    if n%1==0:
        count+=1
if count==2:
    print(n,"is prime")
else:
    print(n,"is composite")
    
    
    
print()
print()
print()



                                # print all prime and composite:

range1=int(input("enter the first number:"))
range2=int(input("enter the second number:"))
for i in range(range1,range2+1):
    count=0
    prime=0
    for j in range(1,i+1):
        if i % j ==0:
            count +=1
    if count ==2:
        print(i,"no is prime:")
    else:
        print(i,"no is composite")    
        
        
print()
print()
print()




                        # print total no of prime and composite numbers:


range1=int(input("enter the first number:"))
range2=int(input("enter the second number:"))
prime=composite=0
for i in range(range1,range2+1):
    count=0
    for j in range(1,i+1):
        if i % j ==0:
            count +=1
    if count ==2:
        prime+=1
    else:
        composite+=1
print("total no of prime is:",prime)
print("total no of composite is:",composite)