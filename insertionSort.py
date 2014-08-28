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

def insertionSort(a):
	for i in range(1, len(a)):
		tmp = a[i]
		k = i
		while k > 0 and tmp < a[k-1]:
			a[k] = a[k-1]
			k -= 1
		a[k] = tmp

def main():
	A = [18,5,100,3,1,19,6,0,7,4,2]
	insertionSort(A)
	print A

if __name__ == "__main__":
	main()
