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

def cmp(a, b, c, d):
    if (b < c):
        e = '<'
    else:
        e = '>'
    a.append([e, b, c])
    return d
