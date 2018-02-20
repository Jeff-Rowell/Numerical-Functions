import numpy as np

machEp = 2**-52

def luFactor(A, n):
    for j in range(0, n-1):
        for i in range(j + 1, n):
            if abs(A[j, j]) > machEp:
                A[i, j] = A[i, j] / A[j, j]
            else:
                print('Error')
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - (A[i, j] * A[j, k])
    return A

A = np.zeros((3, 3))
for i in range(0, 3):
    A[i,0] = 1 + 3*i
    A[i,1] = 2 + 3*i
    A[i,2] = 3 + 3*i
    A[2,2] = 9
print('Matrix A:\n==========')
print(A)
print()
print('Matrix LU:\n===========')
print(luFactor(A, 3))
