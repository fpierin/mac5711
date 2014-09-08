#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Title:	Selecion Sort
#
# Statement:
# Given a disordered list of integers rearrange it in natural order.
#
# Time complexity of solution:
# 
# Best		-> O(n^2)
# Average	-> O(n^2)
# Worst		-> O(n^2)

from compare import cmp

def selectionsort(aList):
    c = []
    for i in range(len(aList)):
        least = i
	for k in range(i + 1, len(aList)):
	    if (cmp(c, aList[k], aList[least], aList[k] < aList[least])):
	        least = k
	swap(aList, i, least)
    return c

def swap(A,x,y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
