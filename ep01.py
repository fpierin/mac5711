#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Title:	Insertion Sort
#

import sys
import itertools

from insertionSort import insertionsort
from selectionSort import selectionsort

def tree(r):
	print ""
	print r
	print ""

def roads(dl, al):
	r = []
	for p in itertools.permutations(dl):
		l = list(p)
		tmp = list(l)
		o = globals()[al](l)
		d = []
		for x in o:
			h = []
			for y in x:
				h.append(tmp.index(y))
			d.append(h)
			
		r.append(d)
		print tmp, " -> ", d
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

	tree(r)
	
	print ""

if __name__ == "__main__":
   main(sys.argv[1:])
