# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:48:37 2022

@author: 91838
"""
s=[4,2,0,5,6,8,9]
i=0
def bubblesort(d):
    global i
    
    
    
    if len(d)==1:
        print(d,"rr")
        return 
    for u in range(len(d)-1):
        if d[u]>d[u+1]:
            # swapping 
            temp=d[u]
            d[u]=d[u+1]
            d[u+1]=temp
            print(d)
                    
    i=i+1
    if i==len(d):
        return d
    bubblesort(d)
    return d

        
        
        
        
    """" global i 
    print(i,"tt")
    
    if i==len(d)-1:# one of the base case 
        return d
    if d[i]>d[i+1]:# swapping 
        temp=d[i]
        d[i]=d[i+1]
        d[i+1]=temp
        print(d)
        print(d[1:])
        i=i+1
        w=bubblesort(d)
        print(w,"tttt")
        bubblesort(w[:-1])
       # i=0 # putting i=0 to again start from first element
       
        
        return w
    
    i=i+1  #incrementing i usinf global coz its value will remain unchanged even during recursion
    e=bubblesort(d)
    print(e,"rr")"""
print(bubblesort(s),"tt")
        
        
    


