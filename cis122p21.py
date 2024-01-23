'''
CIS 122 Spring 2022 Project 2-1
Author(s): Steven Sanchez-Jimenez
Description: Python Functions; transportation problems. 
'''


def max_trans1(a, b, c):
    '''
    I am calculating the minimum capacity weight that can be transported along
    the 3 different route sections

    >>>max_trans1(1, 2, 3)
    1
    '''
    return min(a, b, c)
   

def max_trans2(a, b, c, d, e):
    '''
    I am taking the maximum weight capacity of the two different routes and
    getting a return of which has a higher maximum capacity

    max_trans2(1, 2, 3, 4, 5)
    4
    '''
    min1 = min(a, b, c)
    min2 = min(d, e)
    return max(min1, min2)
    
print(max_trans1(1, 2, 3))
print(max_trans1(9, 6, 3))
print(max_trans1(0, 0, 0))


print(max_trans2(1, 2, 3, 4, 5))
print(max_trans2(222, 110, 411, 54, 73))
print(max_trans2(0, 0, 0, 0, 0))
