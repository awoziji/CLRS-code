# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:09:23 2019

@author: win 10
"""

def counting_sort(a,b,k):
    length_a = len(a);
    a.insert(0,-1)
    b.insert(0,-1)
    c = [0] * (k+1) #0-k
    print(c)
    j = 1                    
    while(j <= length_a):   
        c[a[j]] = c[a[j]] + 1
        j = j + 1
    i = 1
    while(i <= k):
        c[i] = c[i] + c[i-1]
        i = i + 1
    j = length_a
    print(c)
    print(b)    
    while(j >= 1):
        b[c[a[j]]] = a[j]
        c[a[j]] = c[a[j]] - 1
        j = j - 1
    del b[0]    
        
a = [3,4,5,2,1,8,20,10,12]
b = len(a) * [0]
k = max(a)
counting_sort(a,b,k)

print(b)
