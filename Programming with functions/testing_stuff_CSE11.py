from projectile_motion_calculator import calculate_landing_distance, calculate_angle_of_launch
from math import pi, cos, sqrt, sin, sqrt

# age = 23
# uscit = True
# vote = True if age > 17 and uscit else False
# print(vote)

# values = []
# for i in range(20):
#     values.append(i)

# print(values)


# #List comprehensions
# values = [ i for i in range(20)]
# print(values)

# # Example 3

from functools import reduce

# def main():
#     numbers = [87, 95, 72, 92, 95, 88, 84]
#     func_add = lambda a, b: a + b
#     total = reduce(func_add, numbers)
#     average =  total / len(numbers)
#     print(f"average: {average:.2f}")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

#v, a, g, y
# v = 50
# g = 9.8
# y = 0
# a = 10 
# a *= pi / 180
# x = calculate_landing_distance(v, a, g, y)
# print(x)

# landing_distance = (v * cos(a) * (v * sin(a) + sqrt(2 * g * y + v **2 * (sin(a) ** 2)))) / g
# print(landing_distance)
# print(cos(a))

a,b = calculate_angle_of_launch(344.73, 34 * pi/180, 9.8, 500.0)
print(a)