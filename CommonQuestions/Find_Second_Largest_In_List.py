""" ### Find the Second Largest Number in a List/Array ###
ref: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

Input Format:
The first line contains NN. The second line contains an array AA[] of NN integers each separated by a space.

Output Format:
Output the value of the second largest number.

NOTE: Take note of duplicates and (-ve) values as well
"""

#===============================================================================
# Method 1: Without using built-in functions or Sorting, plain approach
#===============================================================================

"""store largest & 2nd Largest element into two variables"""
def second_highest_1(A):
#     N = int(raw_input().strip())
#     A = map(int, raw_input().strip().split(" "))
    
    largest = A[0]
    sec_largest = -9999999999     #arbitrarily assign a very large -ve number
    
    for i in range(1,len(A)):
        if (A[i] > sec_largest and A[i] != largest):
            sec_largest = A[i]
        if sec_largest > largest:
            largest, sec_largest =  A[i], largest
    
    
    if sec_largest == -99999999:
        print "No second largest"
    else:
        print sec_largest



#===============================================================================
# Method 2: Using in-built functions, NOT using sorting
#===============================================================================

"""Find max element and pop it. Then the max from the remaining is the 2nd largest element"""
def second_highest_2(A):
#     N = int(raw_input().strip())
#     A = map(int, raw_input().strip().split(" "))
    
    A = set(A)          #set() removes duplicates, in python
    largest = max(A)
    A.remove(largest)   #remove the largest element
    print max(A)        #second largest
    

#===============================================================================
# Method 3: Using List Comprehensions
#===============================================================================
"""same as above, just instead of remove operations, we create another list without the max element"""

def second_highest_3(A):
#     N = int(raw_input().strip())
#     A = map(int, raw_input().strip().split(" "))
    
    A = [x for x in A if x!= max(A)]    #removing the max item
    print max(A)
    



### DRIVER FUNCTION
A = [1, 3, 5, 6, 6]
B = [1, -5, 4, 2, 5, 4]
C = [3, 3, -2, -4, -5]

second_highest_1(A)
second_highest_1(B)
second_highest_1(C)

print "\n"

second_highest_2(A)
second_highest_2(B)
second_highest_2(C)

print "\n"

second_highest_3(A)
second_highest_3(B)
second_highest_3(C)


   
