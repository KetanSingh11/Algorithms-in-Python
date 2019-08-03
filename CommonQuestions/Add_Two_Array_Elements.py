"""
::QUESTION::
Write a program to add the corresponding elements of two arrays, each of same size and print the sums.
can be any integer between 1 and 100.

#:Example:
>Input:
4
1 2 3 4
5 6 7 8

>Output:
6 8 10 12
"""

N = int(input("Size: "))

# Get the arrays
numArray1 = list(map(int, input("A=").split()))
numArray2 = list(map(int, input("B=").split()))

sumArray = []

# Calculate the sum in one line
sumArray = [p + q for p, q in zip(numArray1, numArray2)]

# Print the sumArray
print(sumArray)
