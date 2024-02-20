n=int(input("enter the number:"))
if n>0:
    print("no is Positive:")
elif n<0:
    print("no is Negative:")
else:
    print("no is equal to Zero")
    
    
    
# using function

def odd(n):
    if n%2==0:
        return True
    else:
        return False

n=int(input("enter the number:"))
print(odd(n))