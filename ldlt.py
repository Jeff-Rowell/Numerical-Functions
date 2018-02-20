import numpy as np

# LDLT Factorization
def ldlt(A):
	m,n = A.shape
	if m!=n:
		quit()
	L = np.matrix(np.zeros((n,n)))
	D = np.matrix(np.zeros((n,n)))
	v = np.zeros((n,1))
	for i in range(0,n):
		L[i,i] = 1.0
		for j in range(0,i):
			v[j] = L[i,j]*D[j,j]
		D[i,i] = A[i,i]
		for j in range(0,i):
			D[i,i] -= L[i,j]*v[j]
		for j in range(i+1,n):
			L[j,i] = A[j,i]
			for k in range(0,i):
				L[j,i] -= L[j,k]*v[k]
			L[j,i] /= D[i,i]
	return L,D
