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
# Best		-> O(n*log(n))
# Average	-> O(n*log(n))
# Worst		-> O(n*log(n))

def merge(x, y):
	if (x == []):
		return y
	elif (y == []):
		return x
	else:
		if x[0] < y[0]:
			return [x[0]] + merge(x[1:], y)
		else:
			return [y[0]] + merge(x, y[1:])

def mergeSort(a):
	if len(a) <= 1:
		return a
	else:
		mid = len(a) // 2
		return merge(mergeSort(a[:mid]),mergeSort(a[mid:]))

def main():
	A = [18,5,100,3,1,19,6,0,7,4,2]
	B = mergeSort(A)
	print B

if __name__ == "__main__":
	main()
