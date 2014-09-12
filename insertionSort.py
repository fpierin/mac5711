#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Author:	Viviane Bonadia

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
