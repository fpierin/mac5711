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

def merge(x, y, c):
	if (x == []):
		return y
	elif (y == []):
		return x
	else:
		if cmp(c, x[0], y[0], (x[0] < y[0])):
			return [x[0]] + merge(x[1:], y, c)
		else:
			return [y[0]] + merge(x, y[1:], c)

def mergesort(a):
	c = []
	if len(a) <= 1:
		return a
	else:
		mid = len(a) // 2
		return merge(mergesort(a[:mid]),mergesort(a[mid:]), c)
