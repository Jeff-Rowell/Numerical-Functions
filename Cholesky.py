import numpy as np

# Cholesky (LLT) Factorization
def chol(A):
	m,n = A.shape
	if m!=n:
		quit()
	L = np.matrix(np.zeros((n,n)))
	for i in range(0,n):
		L[i,i] = np.sqrt(A[i,i])
	for j in range(1,n):
		L[j,0] = A[j,0]/L[0,0]
	for i in range(1,n):
		L[i,i] = A[i,i]
		for k in range(0,i):
			L[i,i] -= L[i,k]**2
		L[i,i] = np.sqrt(L[i,i])
		for j in range(i+1,n):
			L[j,i] = A[j,i]
			for k in range(0,i):
				L[j,i] -= L[j,k]*L[i,k]
			L[j,i] /= L[i,i]
	return L

def potrf(A):
	m,n = A.shape
	if m!=n:
		quit()
	L = np.matrix(np.zeros((n,n)))
	for k in range(0,n):
		L[k,k] = np.sqrt(A[k,k])
		L[k,k+1:n] = (1/L[k,k])*A[k,k+1:n]
		A[k+1:n,k+1:n] -= L[k,k+1:n].T*L[k,k+1:n]
	return L.T
