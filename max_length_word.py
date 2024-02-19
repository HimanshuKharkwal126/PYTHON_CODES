
a=input("enter the string:")
word=a.split(" ")
max=word[0]
for i in range(len(word)):
    if len(word[i])>len(max):
        max=word[i]
print("maximum length word is:",max)
