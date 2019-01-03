# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:34:37 2018

@author: hejianguo
"""

def insert_sort(a):
    j=2
    for j in range(j,len(a)):
        key = a[j]
        i = j-1
        while(i > 0 and a[i]>key):
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
    return a    
        

a = [1,6,3,4,2]

b = insert_sort(a)        