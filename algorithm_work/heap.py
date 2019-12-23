#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/23
# @Author     : S1mple
#
# Description :
import math

def max_heapify(lt, i):
	l = i*2
	r = i*2 + 1
	if l <= len(lt) and lt[l-1] > lt[i-1]:
		largest = l
	else: 
		largest = i
	if r <= len(lt) and lt[r-1] > lt[largest-1]:
		largest = r
	if largest != i:
		lt[i-1], lt[largest-1] = lt[largest-1], lt[i-1]
		max_heapify(lt, largest)


if __name__ == "__main__":
	lt = [16, 4, 10, 14 ,7, 9, 3, 2, 8, 1]
	max_heapify(lt, 2)
	print(lt)
