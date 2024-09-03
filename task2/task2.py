import sys
import math

circle_data = sys.argv[1]
points_data = sys.argv[2]
with open(circle_data, 'r') as file:
    first_line = file.readline().strip().split()
    x_сentre = float(first_line[0])
    y_сentre = float(first_line[1])
    radius = float(file.readline().strip())
with open(points_data, 'r') as file:
    for line in file:
        split_line = line.strip().split()
        x_point = float(split_line[0])
        y_point = float(split_line[1])
        if math.isclose((x_point - x_сentre)**2 + (y_point - y_сentre)**2, radius**2):
            print(0)
        elif (x_point - x_сentre)**2 + (y_point - y_сentre)**2 < radius**2:
            print(1)
        else:
            print(2)
