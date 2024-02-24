def sum(n):
    add=0
    for i in range(n,2*n+1):
        add+=1
    print("sum is",add)
    
def sum_n(n):
    add=0
    for i in range(2*n,n+1,-1):
        add+=1
    print("sum is:",add)
    
n=int(input("enter the number:"))
if n>0:
    sum(n)
else:
    sum_n(n)
