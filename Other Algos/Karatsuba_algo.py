# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:46:53 2018

@author: Ketan

Divide-and-Conquer Algorithm Class


The Karatsuba algorithm is a fast multiplication algorithm.
>> https://en.wikipedia.org/wiki/Karatsuba_algorithm
"""

import sys

def karatsuba(num1, num2):

    #base case for recursion
    if (num1 < 10 or num2 < 10):    # in other words, if x and y are single digits
        return num1 * num2

    ## calculates the size of the numbers
    n = max(len(str(num1)), len(str(num2)))
    nby2 = n//2                     # integer cast

    ## breaking the digits sequences about the middle
    a = num1 // 10**nby2
    b = num1 % 10**nby2
    c = num2 // 10**nby2
    d = num2 % 10**nby2


    ## 3 calls made to numbers approximately half the size
    z0 = karatsuba(b, d)
    z2 = karatsuba(a, c)
    z1 = karatsuba(a+b, c+d) - z2 - z0
    
    # this little trick, writing n as 2*nby2 takes care of both even and odd n
    prod = (z2 * 10**(2*nby2)) + (z1 * 10**nby2) + z0
    
    return prod



if __name__ == "__main__":
    print("Starting 'Karatsuba\'s Algorithm'...")

    if len(sys.argv) >= 3:
        print("Result: {0}".format(karatsuba(sys.argv[1], sys.argv[2])))
    else:
        print("Incomplete Arguments Passed. 2 arguments needed!")
        x, y = map(int, input("Enter 2 numbers, space seperated:").split())
        print("Result: {0}".format(karatsuba(x, y)))
        
        