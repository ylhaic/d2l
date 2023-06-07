import torch

#To express a matrix-vector product in code, we use the mv function.
#Note that the column dimension of A (its length along axis 1)
#must be the same as the dimension of x (its length).
#PyTorch has a convenience operator @ that can execute both matrix-vector and matrix-matrix products

A = torch.arange(6, dtype = torch.float32).reshape(2,3)
#m*n matrix
x = torch.tensor([1.,2.,3.])
#n*1
print(A.shape)
print(x.shape)

print(torch.mv(A, x))
print(A@x)
#m*1 matrix