age=int(input("enter the age:"))
weight=float(input("enter the weight in kg:"))
height=float(input("enter the height in ft:"))
name=input("enter the name:")
h_in_mtr=height*30.48/100
bmi=weight/(h_in_mtr*h_in_mtr)
print(name,"is",age,"years old and have",weight,"kg weight and his height is",h_in_mtr,"and his bmi is",bmi)
if(bmi<18):
    print(name,"your bmi is ",round(bmi,2),"and you are underweight:")
elif(bmi>18 and bmi<25):
    print(name,"your bmi is ",round(bmi,2),"and you are normal:")
else:
    print(name,"your bmi is ",round(bmi,2),"and you are overweight:")