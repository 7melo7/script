#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/15
# @Author     : S1mple
#
# Description :

def find_crossing_subarray(lt, low, mid, high):
	left_max_sum = lt[mid]
	left_sum = lt[mid]
	left_index = mid
	for i in range(mid-1,low-1,-1):
		left_sum += lt[i]
		if left_sum > left_max_sum:
			left_index = i
			left_max_sum = left_sum
	# find right max subarray
	right_max_sum = 0
	right_sum = 0
	right_index = mid
	for i in range(mid+1, high+1):
		right_sum += lt[i]
		if right_sum > right_max_sum:
			right_index = i
			right_max_sum = right_sum
	max_sum = right_max_sum + left_max_sum
	return [max_sum, left_index, right_index]


def find_max_subarray(lt, low, high):
	if low == high:
		return [lt[low], low, high]
	else:
		mid = (low + high) // 2
		left = find_max_subarray(lt, low, mid)
		right = find_max_subarray(lt, mid+1, high)
		cross_subary = find_crossing_subarray(lt, low, mid, high)
	if left[0] > right[0] & left[0] > cross_subary[0]:
		return left
	elif right[0] > left[0] & right[0] > cross_subary[0]:
		return right
	else:
		return cross_subary


if __name__ == "__main__":
	stock = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
	result = find_max_subarray(stock, 0, len(stock)-1)
	print(stock[result[1]:result[2]+1])