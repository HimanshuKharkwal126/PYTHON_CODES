# insertion, searching, deletion, traversing, sorting:

li=[]
def insert():
    if len(li)>10:
        print("stack is full")
    else:
        val=int(input("enter the value:"))
        li.append(val)
        print(li)
def search():
    val=input("enter the element:")
    if val in li:
        print("element found:")
    else:
        print("element not found:")
def deletion():
    if len(li)==0:
        print("stack is full:")
    else:
        li.pop()
        print(li)
def traverse():
    for i in range(len(li)):
        print(li[i])
def sorting():
    for i in range(len(li)):
        li.sort()
choice=1
while(choice!=5):
    choice=int(input("press 1 for insertion /n press 2 for searching /n press 3 for deletion /n press 4 for traversing /n press 5 for sorting:"))
    if choice==1:
        insert()
    elif choice==2:
        search()
    elif choice==3:
        deletion()
    elif choice==4:
        traverse()
    elif choice==5:
        sorting()
    elif choice==6:
        break
