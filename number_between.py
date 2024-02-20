import random
def power(n):
    lr=10**(n-1)
    ur=10**n-1
    no=random.randint(lr,ur)
    return no
print(power(3))
