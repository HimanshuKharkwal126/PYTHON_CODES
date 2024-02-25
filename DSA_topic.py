# Insertion , searching and change the priority of element in low mid or high:

                    

high=[]
mid=[]
low=[]
def insertion():
    value=input("enter the value:")
    priority=input("enter the priority::press low mid or high priority:")
    if priority=="low":
        low.append(value)
    elif priority=="mid":
        mid.append(value)
    elif priority=="high":
        high.append(value)
def search():
    value=input("enter the element:")
    if value in high:
        print("element is in highest priority:")
    elif value in mid:
        print("element is in mid priority:")
    elif value in low:
        print("element is in lowest priority:")
def change():
    value=input("enter the value:")
    newPriority=input("press 1 for increasing priority \n press 0 for decreasing priority:")
    if value in low:
        if newPriority=="I":
            low.remove(value)
            mid.append(value)
        elif newPriority=="D":
            print("It is already in lowest priority:")
    if value in mid:
        if newPriority=="I":
            mid.remove(value)
            high.append(value)
        elif newPriority=="D":
            mid.remove(value)
            low.append(value)
    if value in high:
        if newPriority=="I":
            print("It is already in highest priority:")
        elif newPriority=="D":
            high.remove(value)
            mid.append(value)
choice=1
while(choice!=4):
    choice=int(input("enter the choice:\n1-Insertion:\n2-Search:\n3-Change priority:"))
    if choice==1:
        insertion()
    elif choice==2:
        search()
    elif choice==3:
        change()
    elif choice==4:
        break
    else:
        print("enter valid choice:")
        
