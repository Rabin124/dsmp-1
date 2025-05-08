# Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n = int(input("Enter a number: "))
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i ** 2
print("The sum of squares of first", n, "natural numbers is:", sum_of_squares)