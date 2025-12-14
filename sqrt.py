import math
a=float(input("enter 1st side of traingle\n"))
b=float(input("enter 2nd side of traingle\n"))
c=float(input("enter 3rd side of traingle\n"))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("area :",area)

