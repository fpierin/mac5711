#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Title:	HeapSort
#
# Statement:
# Given a disordered list of integers rearrange it in natural order.
#
# Time complexity of solution:
# 
# Best		-> O(n*log(n))
# Average	-> O(n*log(n))
# Worst		-> O(n*log(n))

from compare import cmp

def quicksortCmp(c, toSort):
    if len(toSort) <= 1:
        return toSort
 
    end = len(toSort) - 1
    pivot = toSort[end]
 
    low = []
    high = []
 
    for num in toSort[:end]:
        if  cmp(c, num, pivot, (num <= pivot)):
            low.append(num)
        else:
            high.append(num)
 
    sortedList = quicksortCmp(c, low)
    sortedList.append(pivot)
    sortedList.extend(quicksortCmp(c, high))
    return sortedList 
		
def quicksort(A):
	c = []
	x = quicksortCmp(c, A)
	return c
