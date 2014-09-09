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

class Node:
	def __init__(self, value):
		self.left = None	
		self.right = None	
		self.value = value
	
	def merge(self, branch):
		print "branch --> ", branch
		if branch:
			triple = branch[0]
			signal = triple[0]
#			node = Node(value)

			if self.value == None:
				value = str(triple[1]) + ":" + str(triple[2])
				self.value = value
			elif signal == "=":
				print "triple ", triple
				value = str(triple[1])
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
		if (self.value != None and self.value.strip() != ""):
			for z in range(i):
				x += "  "
			x += "|-" + self.value
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

def roads(dl, al):
	r = []
	for p in itertools.permutations(dl):
		l = list(p)
	branch = list(l)
	o = globals()[al](l)
	d = []
	for x in o:
		h = []
		for y in x:
			if (str(y) == "<" or str(y) == ">"):
				h.append(y)
			else:
				h.append(branch.index(y))
	    	d.append(h)
	    z = ""
			for h in range(len(dl)):
				z += str(dl.index(h))
			d.append(['=',z])
	r.append(d)

    return r;
		
def main(argv):
	n = int(argv[0])
	a = str(argv[1]).lower()
	print ""
	print "A: ", a
	print "N: ", n
	print ""
	
	l = range(0, n)
	r = roads(l, a)
	print "roads ", r

	print ""	
	t = maketree(r)
	x = t.tree(0)
	print x
	print ""

if __name__ == "__main__":
   main(sys.argv[1:])
