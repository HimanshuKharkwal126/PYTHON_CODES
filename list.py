
list=[2,5,8,6,14,56,45,25,36]
print(len(list))
print()
del list[2:4]                         # for deleting second element of list
print(list)
print()
print(list.index(45))                 # print the index of the given element
print(list.append(20))                # print non value and append value at last
print(list.insert(5,4))               # insert value at given index

list2=[25,50,83]
list.append(list2)                    # for adding 2nd list at last as same as list
list.extend(list2)                    # for adding 2nd list elements at last with 1st last

list3=[2,3,4,5,6,45]
print(list3.pop(2))
list3.remove(6)                       # for deleting given element
print(list3)
list3.clear()                         # for deleting all elements of list

list4=[2,5,8,7,69,15]
print(list4.reverse())                 # for reversing list
print(list4.sort())                    # for assending order
print(list4.count(15))                 # for counting the given no:
print(max(list4))                      # for printing maximum value element
print(min(list4))                      # for printing minimum value element





# for printing list of multiples of 3 and 9

li=[]
for i in range(1,101):
    if i%3==0:
        li.append(i)
print(li)




#addition of two  list

a=[1,2,3,4]
b=[4,5,6,7]
c=[]
for i in range(len(a)):
    value=a[i]+b[i]
    c.append(value)
print(c)
