n=input("enter the 12 digit number:")
print("+",n[0:2],"-",n[2:5],"-",n[5:8],"-",n[8:12])
if n>=str(12):
    print("valid Number:")
else:
    print("Invalid Number:")