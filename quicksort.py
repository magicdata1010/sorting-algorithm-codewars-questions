# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:57:40 2022

@author: 91838
"""
#def quick_sort(arr):
    
  #  quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):
    
    if first<last:
        

        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)


def partition(arr,first,last):
    
    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp


    return rightmark
s=[54,26,93,17,77,31,44,55,20]
print(quick_sort_help(s,0,len(s)-1))
print(s)



