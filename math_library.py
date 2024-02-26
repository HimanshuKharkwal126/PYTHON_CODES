import math

print(math.sqrt(5))
print(math.pow(2,3))
print(math.ceil(3.59))               # for taking higher value
print(math.floor(3.2))               # for taking base value
print("value of log 10 is:",math.log(10))
print("value of log10 10 is:",math.log10(10))
r=180/math.pi                        # change radian to degree
print(math.sin(r))
ra=90*(math.pi/100)                  # change degree to radian
print(math.sin(ra))

d=math.radians(45)
print(math.tan(d))
print("factorial value of 5 is:",math.factorial(5))
print(math.gcd(5,15,20))             # greatest common devider
print(math.fmod(18,4))             # for remainder
print(math.fabs(-25))              # for taking mines common


print(divmod(5,2))                 # return quotient and remainder
print(sum([5,10,28]))
a=15
print("hexadecimal value of 15 is:",hex(a))
print("octal value of 15 is:",oct(a))
print("binary value of 15 is:",bin(a))
c=0o15
print(c)                          # print octal value:
print(round(3.25))
print(int(3.25))