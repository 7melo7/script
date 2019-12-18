#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Time       : 2019/12/18
# @Author     : S1mple
#
# Description :

def echo_matrix(M):
	for i in range(len(M)):
		for j in range(len(M[i])):
			print(str(M[i][j]) + "\t", end="")
		print()

def square_matrix_multiply(A, B):
	C = [[0 for m in range(len(B[0]))] for n in range(len(A))]
	for n in range(len(A)):
		for m in range(len(B[0])):
			C[n][m] = 0
			for j in range(len(A[0])):
				C[n][m] += A[n][j] + B[j][m]
	return C


if __name__ == "__main__":
	A = [[1, 2], [3, 4]]
	echo_matrix(A)
	C = square_matrix_multiply(A, A)
	echo_matrix(C)