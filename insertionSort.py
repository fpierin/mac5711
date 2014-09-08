#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Title:	Insertion Sort
#
# Statement:
# Given a disordered list of integers rearrange it in natural order.
#
# Time complexity of solution:
# 
# Best		-> O(n)
# Average	-> O(n^2)
# Worst		-> O(n^2)

from compare import cmp

def insertionsort(a):
	c = []
	for i in range(1, len(a)):
		tmp = a[i]
		k = i
		while k > 0 and cmp(c, tmp, a[k-1], (tmp < a[k-1])):
			a[k] = a[k-1]
			k -= 1
		a[k] = tmp
	return c
