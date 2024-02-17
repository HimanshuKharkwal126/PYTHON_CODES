def feet_inch(feet):
    return feet*12
def receive():
    feet=int(input("enter the feet:"))
    return feet
def output(o):
    print(o)
output(feet_inch(receive()))