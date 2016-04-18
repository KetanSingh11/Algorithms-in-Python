#===============================================================================
""" Insertion Sort - Implemented in Python """
#===============================================================================

"""shift optimized"""
def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i-1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                break
        A[k+1] = curNum
    
        

#driver Function
A = [5,4,3,2,1]
print A
insertion_sort(A)
print A
