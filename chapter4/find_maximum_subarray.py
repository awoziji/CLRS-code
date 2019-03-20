# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:24:58 2018

@author: steven
"""
import math

def find_maximum_subarray(a,low,high):
    if high == low:
        return (low,high,a[low])
    else:
        mid = math.floor((low+high)/2)
        (left_low,left_high,left_sum) = find_maximum_subarray(a,low,mid)
        (right_low,right_high,right_sum) = find_maximum_subarray(a,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(a,low,mid,high)
        if left_sum >=right_sum and left_sum >=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
        
def find_max_crossing_subarray(a,low,mid,high):
    left_sum = -9999999
    sum = 0
    i = mid
    while(i>=low):
        sum = sum + a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
        i = i - 1    
    right_sum = -99999999
    sum = 0
    j = mid + 1
    while(j<=high):
        sum = sum + a[j]
        if sum >right_sum:
            right_sum = sum
            max_right = j
        j = j + 1    
    return (max_left,max_right,left_sum + right_sum)


a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
b = find_maximum_subarray(a,0,len(a)-1)
