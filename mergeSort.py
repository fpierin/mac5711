#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Title:	MergeSort
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

def merge(c, x, y):
	if (x == []):
		return y
	elif (y == []):
		return x
	else:
		if cmp(c, x[0], y[0], (x[0] < y[0])):
			return [x[0]] + merge(c, x[1:], y)
		else:
			return [y[0]] + merge(c, x, y[1:])
			
def mergesortCmp(c, a):
	if len(a) <= 1:
		return a
	else:
		mid = len(a) // 2
		return merge(c, mergesortCmp(c, a[:mid]), mergesortCmp(c, a[mid:]))
		
def mergesort(a):
	c = []
	x = mergesortCmp(c, a)
#	print c
# return x
	return c

def main():
	A = [18,5,100,3,1,19,6,0,7,4,2]
	B = mergesort(A)
	print B

if __name__ == "__main__":
	main()
