# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:15:51 2018

@author: hejianguo
"""
import math
import sys

MAX_INT = sys.maxsize

def merge_sort(a,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)

def merge(a,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1+1+1)
    R = [0] * (n2+1+1)
    i = 1
    j = 1
    while(i <=n1 ):
        L[i] = a[p + i -1]
        i = i + 1
    while(j <=n2 ):
        R[j] = a[q + j]
        j = j + 1
    L[n1+1] = MAX_INT #无穷大
    R[n2+1] = MAX_INT #无穷大
    i = 1
    j = 1
    k=p
    while(k<=r):
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j+ 1
        k = k + 1    


def merge_sort_py_style(a):
    if len(a) == 1:
        return a
    q = math.floor(len(a)/2)
    l = merge_sort_py_style(a[:q])
    r = merge_sort_py_style(a[q:])
    return merge_py_style(l,r)

def merge_py_style(l,r):
    i = 0
    j = 0
    l.append(99999)
    r.append(99999)
    res = []
    for k in range(0,len(l)+len(r)-2):
        if l[i] <= r[j]:
            res.append(l[i])
            i = i + 1
        else:
            res.append(r[j])
            j = j + 1       
    return res        

a = [8,5,4,9,3,7,2,1]
merge_sort(a,0,len(a)-1)    
#b = merge_sort_py_style(a)
#print(b)
