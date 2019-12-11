#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/11
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


def insertionSort(lt):
	for i in range(1,len(lt)):
		j = i - 1
		key = lt[i] 
		while j >= 0 and key < lt[j]:
			lt[j+1] = lt[j] 
			j = j - 1
		lt[j+1] = key
	return lt

if __name__ == "__main__":
	print("This is a script used to sort a list of numbers by insertion sort.")
	unsort_list = usr_input()
	print("your numbers list looks like this:")
	for i in unsort_list: print(str(i)+' ', end='')
	sorted_list = insertionSort(unsort_list)
	print('')
	print("After insertion sort, your numbers list looks like this:")
	for i in sorted_list: print(str(i)+' ', end='')
	print('')