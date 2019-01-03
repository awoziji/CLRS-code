# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 14:46:50 2018

@author: win 10
"""
import math
import ctypes

def parent(i):
    return math.floor(i/2)

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def max_heapify(a,i,heapsize):
    l = left(i)
    r = right(i)
    if l < heapsize and a[l] > a[i]: #数组下标从0算,最大为length-1
        largest = l
    else:
        largest = i
    if r < heapsize and a[r] > a[largest]: #数组下标从0算，最大为length-1
        largest = r
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        max_heapify(a,largest,heapsize)
        
def build_max_heap(a):
    heapsize = len(a)
    i = math.floor(len(a)/2) - 1 #数组下标从0算-1
    while(i>=0):   #数组下标从0算-1
        max_heapify(a,i,heapsize)
        i = i - 1
        
def heap_sort(a):
    build_max_heap(a)
    i = len(a) - 1 #数组下标从0算-1
    heapsize = len(a)
    while(i>=1):    #数组下标从0算-1
        a[0],a[i] = a[i],a[0]
        heapsize = heapsize - 1
        max_heapify(a,0,heapsize)
        i = i - 1


a = [4,3,6,8,9,7,1,2] 
heap_sort(a)
print(a)       
        

    