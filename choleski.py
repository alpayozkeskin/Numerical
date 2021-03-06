from __future__ import division
import numpy as np
import math

def choleski(a):
    a = a.astype(float)
    n = len(a)
    for i in range(n):
        try:
            a[i, i] = math.sqrt(a[i, i] - np.dot(a[i, 0:i], a[i, 0:i]))
        except ValueError:
            print a[i, i]
            print 'Matrix is not positive definite'
        for j in range(i + 1, n):
            a[j, i] = ((a[j, i] - np.dot(a[j, 0:i],a[i, 0:i]))
            / a[i, i])
    for i in range(0, n - 1):
        a[i, i + 1:n] = 0
    return a


def choleski_sol(L, b):
    n = len(b)
    



def init():
    a = np.array([(4,-2,2),(-2,2,-4),(2,-4,11)])
    b = np.array([11,-16,17])
    a = choleski(a)
   # b = lu_solve(a, b)
    print a
   # print b


init()
            
