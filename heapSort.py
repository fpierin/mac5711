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

def heapsortCmp(c, A):

	def heapify(c, A):
		start = (len(A) -2) / 2
		while (start >= 0):
				fixdown(c, A, start, len(A) - 1)
				start -= 1
	
	def fixdown(c, A, start, end):
		root = start
		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if (child + 1 <= end and cmp(c, A[child], A[child + 1], (A[child] < A[child + 1]))):
				child += 1
			if (child <= end and cmp(c, A[root], A[child], (A[root] < A[child]))):
				A[root], A[child] = A[child], A[root]
				root = child
			else:
				return

	heapify(c, A)
	end = len(A) - 1
	while end > 0:
		A[end], A[0] = A[0], A[end]
		fixdown(c, A, 0, end -1)
		end -= 1

def heapsort(A):
	c = []
	x = heapsortCmp(c, A)
	return c
