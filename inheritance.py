
class person:                               # parent class:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showname(self):
        print("name is:",self.name)
    def showage(self):
        print("age is:",self.age)

class student(person):                      # child class:
    def __init__(self,r,c):
        person.__init__(self,"himanshu",19)
        self.rollno=r
        self.course=c
    def showrollno(self):
        print("roll no is:",self.rollno)
    def showcourse(self):
        print("course is:",self.course)
s1=student(100,"B.Tech")
s1.showrollno()                             # reference variable:
s1.showcourse()
s1.showage()
s1.showname()


"""

class cloth:
    def __init__(self,c,b):
        self.color=c
        self.brand=b
class shirt(cloth):
    def __init__(self,s,n):
        cloth.__init__(self,"black","Adidas")
        self.sleeve=s
        self.neck=n
    def showdetails(self):
        print("color is:",self.color)
        print("brand is:",self.brand)
        print("sleeve is:",self.sleeve)
        print("neck is:",self.neck)
s2=shirt("sleeveless","round")
s2.showdetails()


"""