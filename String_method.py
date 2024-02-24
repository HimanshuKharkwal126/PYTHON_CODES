a="!!!!!himanshu!!!!!!!!!!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.lstrip("!"))
print(a.replace("himanshu","harshit"))
print(a.split("h"))                       # breaks the sting in form of list

print()


b="harshitharshithimmu"
print(b.capitalize())
print(b.center(20))                       # adds space in starting
print(b.count("harshit"))
print(b.endswith("himmu"))
print(b.endswith("himmu",10,20))


print()

c="hello my name is himanshu"
print(c.find("is"))
print(c.index("my"))
print(c.istitle())
print(c.swapcase())
print(c.title())



str="hello"
str1="world"
a="*".join(str)
print(a)
b="$".join(str1)
print(b)
s="i am doing python programming"
l=s.split("o")                     # remove o from string
print(l)
p=s.replace("python","java")       # place java in place of python
print(p)