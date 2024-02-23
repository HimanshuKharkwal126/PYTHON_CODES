
# for upper count,lower count and digits:


str=input("enter the string:")
ul=lc=dc=0
w=1
for i in str:
    if i.isupper():               # for upper count
        ul+=1
    elif i.islower():             # for lower count
        lc+=1
    elif i.isdigit():             # for digit count
        dc+=1
    elif i.isspace():             # for space count
        w+=1
print("upper count is:",ul)
print("lower count is:",lc)
print("digit count is:",dc)
print("space count is:",w)