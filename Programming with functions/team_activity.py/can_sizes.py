"""
Team activity 1/23/2023
-Seth Ricks
"""

from math import pi



def main():
    count = 0
    can_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "211", "300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    hieght = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]


    for can_names in can_names:
        print(can_names, end= " ")
        storage_efficiency = compute_volume(radius[count], hieght[count]) / compute_surface_area(radius[count], hieght[count])
        cost_efficiency = compute_cost_efficiency(compute_volume(radius[count], hieght[count]), costs[count])
        print(f"{storage_efficiency:.2f}- {cost_efficiency:.2f}")
        count += 1


def compute_volume(radius, height):
    volume = pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def compute_cost_efficiency(volume, costs):
    cost_efficiency = volume / costs 
    return cost_efficiency

main()

"""

Compound list of lists 

 # A compound list (a list that contains lists).
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]
"""