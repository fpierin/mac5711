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

def selectionSort(aList):
	for i in range(len(aList)):
		least = i
		for k in range(i + 1, len(aList)):
			if (aList[k] < aList[least]):
				least = k
		swap(aList, i, least)
		
def swap(A,x,y):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp

def main():
	A = [18,5,100,3,1,19,6,0,7,4,2]
	selectionSort(A)
	print A

if __name__ == "__main__":
	main()