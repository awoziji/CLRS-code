# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:14:01 2018

@author: steven
"""

def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)

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


a = [2,3,8,6,5,7,1]

quick_sort(a,0,len(a)-1)

print(a)
