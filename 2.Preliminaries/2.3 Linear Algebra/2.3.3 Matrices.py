#Just as scalars are 0th-order tensors and vectors are 1st-order tensors
#matrices are 2nd-order tensors. We denote matrices by bold capital letters
#(e.g., X, Y, and Z), and represent them in code by tensors with two axes.
import torch

A = torch.arange(6).reshape(3, 2)
print(A)
#Output:
#tensor([[0, 1],
#        [2, 3],
#        [4, 5]])  3 rows and 2 columns
#Transpose: exchange matrix's rows and columns, m*n matrix to n*m matrix
B = A.T
print(B)
#if B = A^T, a(i,j) -> b(j,i)
for i in range(len(A)):
    for j in range(len(A[0])):
        print(A[i, j] == B[j, i])
#Symmetric matrices are the subset of square matrices that are equal to their own transposes
C = torch.tensor([[0, 1, 2], [1, 3, 4], [2, 4, 5]])
print(C == C.T)
