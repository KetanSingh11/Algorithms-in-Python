# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:05:51 2018

@author: Ketan

Divide-and-Conquer Algorithm
=============================
        MERGE SORT
=============================
"""

def merge(left, right):
    ## merge step - merge left + right into result
    
    result = []
    i = 0   #counter for left
    j = 0   #counter for right
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif (right[j] < left[i]):
            result.append(right[j])
            j +=1
        
    #append the remaining of the left/right elements
    result += left[i:]
    result += right[j:]
    
    return result
            


def sort(seq):
    """
    Takes a list of numbers and sorts in ascending order
    """
    
    if len(seq) <= 1:
        return seq
    
    middle = len(seq)//2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    
    return merge(left, right)



if __name__ == "__main__":
    
    li = [5,3,2,1000,54,45,4]
    print("Result:")
    print(sort(li))
    