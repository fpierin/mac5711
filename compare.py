#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Author:	Viviane Bonadia

def cmp(a, b, c, d):
    if (b < c):
        e = '<'
    elif (b > c):
        e = '>'
    else:
    	return
    a.append([e, b, c])
    return d
