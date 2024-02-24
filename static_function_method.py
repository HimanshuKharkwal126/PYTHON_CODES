
class Student:
    a=10                             # first method:
    def __init__(self):
        self.x=20                    # instance variable:
        Student.b=20                 # second method:
    @staticmethod                    # class method: static method can be call by object name or class name:
    def f1(m,n):                     # static method || static member function:
        Student.c=30                 # third method:
        print("hello")
    def f2(self,a):                  # instance member function || instance method:
        Student.d=50                 # fourth method:
    @classmethod
    def f3(cls):
        cls.e=50                     # fifth method:
        Student.f=60                 # sixth method:
        print("class method")
Student.g=70                         # static variable:
s1.Student()
Student.f1(2,3)                      # class name = static: || with self function = instance:
Student.f2(5,6)
Student.f3()
print(Student.__dict__)              # used for know about all types of members,function,variables: