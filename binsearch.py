# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:51:33 2018

@author: 14464
"""
import math
def binSearch(array,key,begin,end):
    if begin > end : return -1
    mid = (end + begin)//2
    if key == array[mid]:
        return mid
    
    elif key>array[mid]:
        return binSearch(array,key,mid+1,end)
    else:
        return binSearch(array,key,begin,mid-1)
   

def binarySearchDG(x, arr, low, high):#递归算法
    if low > high: return -1
 
    mid = (low+high)//2
    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return binarySearchDG(x, arr, low, mid-1)
    else:
        return binarySearchDG(x, arr, mid+1, high)

def mergeSort(array,begin,end):
    if end > begin:
        mid = math.floor((begin+end)/2)
        merge(array,begin,mid,end)
        mergeSort(array,begin,mid)
        mergeSort(array,mid+1,end)

def merge(array,begin,mid,end):
    Left = [0 for i in range(mid-begin+2)]
    Right = [0 for i in range(end+mid+1)]
    for i in range(mid-begin+1):
        Left[i] = array[i+begin]
    for j in range(end-mid):
        Right[i] = array[j+mid+1]
    Left[-1] = float('inf')
    Right[-1] = float('inf')
    l = 0
    r = 0
    for k in range(len(array)):
        if Left[l] > Right[r]:
            array[k] = Right[r]
            r+=1
        else:
            array[k] = Left[l]
            l+=1
            
            