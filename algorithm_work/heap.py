#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/23
# @Author     : S1mple
#
# Description :
import random
# 维护最大堆
def max_heapify(heap, HeapSize, root):
  left = 2 * root + 1
  right = left + 1
  larger = root
  if left < HeapSize and heap[larger] < heap[left]:
    larger = left
  if right < HeapSize and heap[larger] < heap[right]:
    larger = right
  if larger != root:
    heap[larger], heap[root] = heap[root], heap[larger]
    max_heapify(heap, HeapSize, larger)
#初始化最大堆
def build_max_heap(heap):
  HeapSize = len(heap)
  for i in range((HeapSize - 2) // 2, -1, -1):
    max_heapify(heap, HeapSize, i)

def heap_sort(heap):
  build_max_heap(heap)
  for i in range(len(heap)-1, -1, -1):
    heap[0], heap[i] = heap[i], heap[0]
    max_heapify(heap, i, 0)
  return heap

if __name__ == "__main__":
	lt = [12, 11, 13, 5, 6, 7]
	print(lt)
	heap_sort(lt)
	print(lt)
