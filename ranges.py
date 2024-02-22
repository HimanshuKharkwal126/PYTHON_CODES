# for i in range(0,5,1):                     # 0 se 15 k beech 1 - 1 k gap m no print kro
for i in range(0,15,2):                      # 0 se 15 k beech 1 - 1 k gap m no print kro
    print(i,end=" ")                         # end=" "  is used for no change in line in a loop
print()
print()
s="himanshu"
for i in range(len(s)):
    print(s[i],end=" ")
print()
print("length of string is",len(s))
print()
print()
s="himanshu"
for i in range(len(s)-1,0,-1):              #  reverse the letters of string from 1 position
    print(s[i],end=" ")



s="himanshu"
for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")                     #  reverse the letters of string from 0 position
