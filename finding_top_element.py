
li=[]
def push():
    val=int(input("enter the number:"))
    li.append(val)
def pop():
    li.pop(0)
    print(li)
def display():
    for i in range(len(li)):
        print(li[i])
def top():
    print(len(li)-1)
choice=1
while(choice!=5):
    choice=int(input("press 1 for adding press 2 for deleting press 3 for display press 4 for top:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        top()
    elif choice==5:
        break
