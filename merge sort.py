# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:01:45 2022

@author: 91838
"""


s=[2,8,5,3,9,4,1,7]

print(s,"uu")
def mergesort(arr):
    if len(arr)==1:
        
        return arr
    subleft=mergesort(arr[:len(arr)//2])
    print(arr)
    print(subleft)
    subright=mergesort(arr[len(arr)//2:])
    mergelist= subleft+subright
    print(mergelist,"yy")
    mergelist.sort()
    return mergelist
print(mergesort(s))
