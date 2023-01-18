import math
t_area = lambda base, height : 0.5*base*height
r_area = lambda length, breadth : length*breadth
s_area = lambda side : side**2
c_area = lambda radius : math.pi*radius*radius
# invoke lambda functions and print results.
print("\n")
print("Area of Triangle (10,5) is:", t_area(10,5))
print("Area of Rectangle (30,20) is:", r_area(30,20))
print("Area of Square (5) is:", s_area(5))
print("Area of circle (7) is:", c_area(7))
