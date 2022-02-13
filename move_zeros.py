# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:57:30 2022

@author: 91838
"""
def move_zeros(array):
    l=0
    print(array)
    if array==[]:
        return []
    for r in range(len(array)):
        if array[r]!=0: # swapping ,using dyanmic changing nature of list
            array[r],array[l]=array[l],array[r]
            l=l+1
    return array



