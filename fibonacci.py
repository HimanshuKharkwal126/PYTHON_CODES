  # using list 
a=0
b=1
li=[]
li.append(a)
li.append(b)
n=int(input("enter the total no of elements you want to see in series:"))
for i in range(n-2):
    c=a+b
    a=b
    b=c
    li.append(c)
print(li)
