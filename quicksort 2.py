# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:44:56 2022

@author: 91838
"""




def partition(arr,lb,ub):
    pivot=arr[lb]
    start=lb
    end=ub
    while start<end:
        
       while arr[start]< arr[lb]:
        start=start+1
       while arr[end]>arr[lb]:
        end=end-1
       if start<end:
        temp=arr[end] #swapping
        arr[end]=arr[start]
        arr[start]=temp
    print(s,"tt",end,start,s)
    o=arr[end]
   # arr[end]=pivot
    #pivot=o
    print(arr[end],pivot,s)
    t=arr[lb]
    arr[lb]=arr[end]
    arr[end]=t
    print(arr[end])
    return end
#print(partition(s,0,len(s)-1))
print(s)
def quicksort(arr,l,r):
   # if len(arr)==1:
       
    
    if l<r:
        sp=partition(arr,l,r)
        quicksort(arr,l,sp-1)
        quicksort(arr,sp+1,r)
    #return     
    
s=[54,26,93,17,77,31,44,55,20]    
print(quicksort(s,0,len(s)-1))        
        



