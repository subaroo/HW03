#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare

def compare(x, y):
    if  x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1



################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.

import math

def hypotenuse(leg_a, leg_b):
    hypotenuse_squared = leg_a ** 2 + leg_b ** 2 
    len_hypotenuse = math.sqrt(hypotenuse_squared)
    return len_hypotenuse



################################################################################
# Exercise 3
# When you submit only include your final function: is_between

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False



################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(rest_of_word(word))



################################################################################
# Exercise 7
# When you submit only include your final function: is_power

#lost
def is_power(a, b):
    x
    a % b = b ** x :
    if a % b = 0 && 
        if 



################################################################################
def main():
    # Exercise 1
    compare(1,1)
    compare(1,2)
    compare(2,1)
    # Exercise 2
    hypotenuse(1,1)
    hypotenuse(3,4)
    hypotenuse(1.2,12)
    # # Exercise 3
    is_between(1,2,3)
    is_between(2,1,3)
    is_between(3,1,2)
    is_between(1,1,2)
    # Exercise 6
    is_palindrome("Python")
    is_palindrome("evitative")
    is_palindrome("sememes")
    is_palindrome("oooooooooooo")


    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")


    ############################################################################
    # Uncomment the below to test and before commiting:
  
   
   
   
    # # Exercise 7
    # is_power(28,3)
    # is_power(27,3)
    # is_power(248832,12)
    # is_power(248844,12)


if __name__ == "__main__":
    main()

