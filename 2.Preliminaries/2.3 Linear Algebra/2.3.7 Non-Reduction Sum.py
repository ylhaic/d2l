import torch

#Sometimes it can be useful to keep the number of axes unchanged
#when invoking the function for calculating the sum or mean.
#This matters when we want to use the broadcast mechanism.

A = torch.arange(12, dtype = torch.float32).reshape(3,4)
print(A)
sumA = A.sum(axis = 1, keepdims = True)
print(sumA)
print(sumA.shape)

print(A / sumA)#broadcasting

#If we want to calculate the cumulative sum of elements of A along some axis
#say axis=0 (row by row), we can call the cumsum function.
#By design, this function does not reduce the input tensor along any axis.
print(A.cumsum(axis = 0))
print(A.cumsum(axis = 1))