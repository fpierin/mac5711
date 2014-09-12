#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Author:	Viviane Bonadia

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
