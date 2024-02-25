dict={}
for i in range(2):
    name=input("enter the name:")
    marks=float(input("enter the marks:"))
    dict[name]=marks
print(dict)




# dictionary of  months

dict={"jan":31,"feb":28,"mar":31,"apr":30,"may":31,"june":30,"july":31,"aug":31,"sep":30,"oct":31,"nov":30,"dec":31}
month=input("enter the month:")
print(dict[month])
print()
a=list(dict.keys())
a.sort()                    # for assending order of months:
print(a)
print()
for i in dict:
    if dict[i]==31:
        print(i)
print()
for i in dict:
    if dict[i]==30:
        print(i)
print()
for i in dict:
    if dict[i]==28:
        print(i)