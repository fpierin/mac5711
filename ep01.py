#!/usr/bin/env python
#
# Author: Felipe Lombardi Pierin
# Nusp:	5875242

#             hello
#       +---------------+
#       1               1
#   +-------+       +-------+
#   2       3       2       3
# +---+   +---+   +---+   +---+
# 4   5       6   4   5       6

import sys
import itertools

from insertionSort import insertionsort
from selectionSort import selectionsort
from mergeSort import mergesort

class Node:
	def __init__(self, value):
		self.left = None	
		self.right = None	
		self.value = value
	
	def merge(self, branch):
#		print "branch --> ", branch
		if branch:
			triple = branch[0]
			signal = triple[0]
#			node = Node(value)

			if signal == "=":
				value = str(triple[1])
				self.value = value
			elif self.value == None:
				value = str(triple[1]) + ":" + str(triple[2])
				self.value = value
			if signal == "<":
				if (self.left == None):
					self.left = Node(None)
				self.left.merge(branch[1:])
			elif signal == ">":
				if (self.right == None):
					self.right = Node(None)
				self.right.merge(branch[1:])

		return self

	def tree(self, i):
		x = ""
		l = "-"
		if (self.value != None and self.value.strip() != ""):
			for z in range(i):
				x += "  "
				l += "-"
			x += "|" + l + self.value
			i += 1
		if (self.left is not None):
			lvalue = self.left.tree(i)
			if lvalue != None and lvalue != "":
				x += "\n" + self.left.tree(i)
		if (self.right is not None):
			rvalue = self.right.tree(i)
			if rvalue != None and rvalue != "":
				x += "\n" + self.right.tree(i)
		return x

def make(root, branch):    
    if root is None:
        root = Node(None)
    root.merge(branch)
    return root
		

def maketree(branches):
#    print ""
#    print branches
#    print ""

    root = Node(None)
    for branch in branches:
			root = make(root, branch)

    return root

def roads(defaultList, al):
	roadList = []
	for p in itertools.permutations(defaultList):
		permutation = list(p)
		z = ""
#		print "p ", permutation
		for j in range(len(defaultList)):
			z += str(permutation.index(j))
			
		branch = list(permutation)
		compareList = globals()[al](permutation)
		d = []
		for compare in compareList:
			h = []
			for value in compare:
				if (str(value) == "<" or str(value) == ">"):
					h.append(value)			
				else:
					h.append(branch.index(value))
			d.append(h)
		d.append(['=',z])
		roadList.append(d)
	return roadList;
		
def main(argv):
	n = int(argv[0])
	a = str(argv[1]).lower()
	print ""
	print "A: ", a
	print "N: ", n
	print ""
	
	l = range(0, n)
	r = roads(l, a)
#	print "roads ", r

	print ""	
	t = maketree(r)
	x = t.tree(0)
	print x
	print ""

if __name__ == "__main__":
   main(sys.argv[1:])
