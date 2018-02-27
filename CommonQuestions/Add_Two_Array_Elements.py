""" Write a program to add the corresponding elements of two arrays, each of size and print the sums.
    can be any integer between 1 and 100.
"""

N = int(input())

# Get the arrays
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Calculate the sum in one line
x = [p + q for p, q in zip(numArray1, numArray2)]

# Print the sumArray
for element in x:
    print(element, end=" ")
