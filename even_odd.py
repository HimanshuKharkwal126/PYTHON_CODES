for i in range(1,25):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")                          


print()
print()
print()



                                #  using function find the given no is even or odd:


def odd(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter the number:"))
print(odd(num))                                        





