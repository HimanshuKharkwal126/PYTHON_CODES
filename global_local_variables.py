x=10
class Student:
    def set(self):
        global x
        x=20
        print("inside class value of x is:",x)
s1=Student()
s1.set()
print("outside function value of x is:",x)