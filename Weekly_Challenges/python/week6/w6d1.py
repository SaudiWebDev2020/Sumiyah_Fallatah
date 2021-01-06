# Recursion
# --------------------------------------------------------------------------------------------------

# rSigma
# --------------------------------------------------------------------------------------------------
# Write a recursive function that, given a number, returns the sum of integers from one up to that number. For example:
# rSigma(5) = 1+2+3+4+5 = 15
# rSigma(2.5) = 1+2 = 3
# rSigma(-1) = 0.
import math

def rSigma(num):
    if num < 0:
        return 0
    else:
        return rSigma(num-1) + math.floor(num)

print(rSigma(5))
print(rSigma(0))
print(rSigma(2.5))


# rFactorial
# --------------------------------------------------------------------------------------------------
# Given a number, return the product of integers from 1 upward to that number. If less than zero, treat as
# zero. If not an integer, treat as an integer. Mathematicians tell us that 0! is equal to 1, so make
# rFact(0) = 1. Examples: 
# rFact(3) = 6 (1*2*3)
# rFact(6.5) = 720 (1*2*3*4*5*6)

# mul = 0 
def rFactorial(num):
    if num < 1:
        return 1
    else:
        return rFactorial(num-1) * math.floor(num)


# print(rFactorial(6.7))
# print(rFactorial(3))
# print(rFactorial(0))

# rBinarySearch
# --------------------------------------------------------------------------------------------------
# Write a recursive function that, given a sorted array and a value, determines whether the value is found within the array. For example,
# rBinarySearch([1,3,5,6], 4) = false
# rBinarySearch([4,5,6,8,12], 5) = true

