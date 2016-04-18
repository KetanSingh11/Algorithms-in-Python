#===============================================================================
""" Insertion Sort - Implemented in Python """
#===============================================================================

"""swap optimized"""
def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i-1, -1, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break
         

#driver Function
A = [5,4,3,2,1]
print A
insertion_sort(A)
print A
