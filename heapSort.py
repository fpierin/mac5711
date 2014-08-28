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

def HeapSort(A):
	def heapify(A):
		start = (len(A) -2) / 2
		while (start >= 0):
				fixdown(A, start, len(A) - 1)
				start -= 1
	
	def fixdown(A, start, end):
		root = start
		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if (child + 1 <= end and A[child] < A[child + 1]):
				child += 1
			if (child <= end and A[root] < A[child]:
				A[root], A[child] = A[child], A[root]
				root = child
			else:
				return

	heapify(A)
	end = len(A) - 1
	while end > 0:
		A[end], A[0] = A[0], A[end]
		fixdown(A, 0, end -1)
		end -= 1
		

def main():
	A = [18,5,100,3,1,19,6,0,7,4,2]
	B = HeapSort(A)
	print B

if __name__ == "__main__":
	main()
