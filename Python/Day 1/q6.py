# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
dog = int(input("Enter the number of dogs: "))
chicken = int(input("Enter the number of chickens: "))
total_heads = dog + chicken
total_legs = (dog * 4) + (chicken * 2)
print("Total heads: ", total_heads)
print("Total legs: ", total_legs)
