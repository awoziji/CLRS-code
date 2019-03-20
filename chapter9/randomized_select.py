# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:28:46 2018

@author: steven
"""
import random
def randomized_select(a, p, r, i):
    if p == r:
        return a[p]
    q = randomized_partition(a, p, r)
    k = q-p+1
    if i==k:
        return a[q]
    elif i < k:
        return randomized_select(a, p, q-1, i)
    else:
        return randomized_select(a, q+1, r, i-k)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    j = p
    while(j <= (r-1)):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j],a[i]
        j = j + 1    
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

def randomized_partition(a, p, r):
    i = random.randint(p,r)
    a[r], a[i] = a[i],a[r]
    return partition(a, p, r)
    
a = [3,2,6,5,7,9,1,4]

b = randomized_select(a, 0, len(a)-1, 8)    

print(b)
