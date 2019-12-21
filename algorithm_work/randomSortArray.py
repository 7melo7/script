#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/21
# @Author     : S1mple
#
# Description :
import random

def permute_by_sorting(lt):
	n = len(lt)
	index = [random.randint(1, n**3) for i in range(n)]
	# insertion sort here
	for i in range(1,n):
		j = i - 1
		key = index[i] 
		while j >= 0 and key < index[j]:
			index[j+1] = index[j]
			j = j - 1
		index[j+1] = key
		lt[j+1], lt[i] = lt[i], lt[j+1]
	return lt

def randomize_in_place(lt):
	n = len(lt)
	for i in range(n):
		random_index = random.randint(i, n-1)
		lt[i], lt[random_index] = lt[random_index], lt[i]
	return lt

if __name__ == "__main__":
	lt = [23, 41, 12, 18, 32, 20]
	print(permute_by_sorting(lt))
	print(randomize_in_place(lt))