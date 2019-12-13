#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/12
# @Author     : S1mple
#
# Description :


def usr_input():
	unsort_list = []
	s = input("Start to enter numbers (y/n):")
	if s == "y" or s == "Y":
		while True:
			t = input("enter a number (q to quit):")
			if t == "q" or t == "Q": return unsort_list
			try:
				t = int(t)
				unsort_list.append(t)
			except Exception as e:
				print("%s is not a number, stop!"%t)
				return unsort_list
	else:
		exit(0)


def merge(a, b):
	c = []
	i = j = 0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			c.append(a[i])
			i += 1
		else:
			c.append(b[j])
			j += 1
	c.extend(a[i:])
	c.extend(b[j:])
	return c

def merge_sort(lts):
	if len(lts) <= 1:
		return lts
	middle = len(lts)//2
	left = merge_sort(lts[:middle])
	right = merge_sort(lts[middle:])
	return merge(left, right)

if __name__ == "__main__":
	print("This is a script used to sort a list of numbers by insertion sort.")
	unsort_list = usr_input()
	print("your numbers list looks like this:")
	for i in unsort_list: print(str(i)+' ', end='')
	sorted_list = merge_sort(unsort_list)
	print('')
	print("After insertion sort, your numbers list looks like this:")
	for i in sorted_list: print(str(i)+' ', end='')
	print('')