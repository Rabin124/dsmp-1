# write a program to find the euclidean distance between two coordinates. Take the coordinates as input from the user.
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The Euclidean distance is: ", distance)