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
			value = str(triple[1]) + ":" + str(triple[2])
			signal = triple[0]
			node = Node(value)

			if self.value == None:
				self.value = value
			elif self.value != value:
				print "diferente ", value

			if signal == "<":
				if (self.left == None):
					self.left = Node(None)
				self.left.merge(branch[1:])
			elif signal == ">":
				if (self.right == None):
					self.right = Node(None)
				self.right.merge(branch[1:])
		return self
	
	def show(self):
		if (self.left is not None):
			self.left.show()
		if (self.value is not None):
			print "+---+"
			print self.value
		if (self.right is not None):
			self.right.show()

def make(root, branch):    
    if root is None:
        root = Node(None)
    root.merge(branch)
    return root
		

def maketree(branches):
    print ""
    print branches
    print ""

    root = Node(None)
    for branch in branches:
		root = make(root, branch)
		print "root -> ", root.value

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
	r.append(d)
	print branch, " -> ", d
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
	
	t = maketree(r)
	t.show()
	print ""

if __name__ == "__main__":
   main(sys.argv[1:])
