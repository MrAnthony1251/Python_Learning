# Exercise 1 ----->  C = 2Rr

import math

radius1 = float(input("Enter the radius of a circle1: "))

circumference1 = 2 * math.pi * radius1

print(f"The Circumference1 is: {round(circumference1, 2)} cm")


# Exercise 2 ----> A = rr²

radius2 = float(input("Enter the radiues of a circle2: "))

area = math.pi * pow(radius2, 2)

print(f"the area of the circle2 is: {area} cm^2")

# Exercise 3 ------->  C = a² + b²

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b, 2))


print(f"Side C = {c}")