import torch

#calculate the sum of a tensor's elements
x = torch.arange(3, dtype=torch.float32)
print(x)
print(x.sum())
A = torch.arange(24, dtype=torch.float32).reshape(3,2,4)
print(A)
print(A.sum())
#By default, invoking the sum function reduces a tensor along all of its axes
#eventually producing a scalar.
#Our libraries also allow us to specify the axes along which the tensor should be reduced.
#To sum over all elements along the rows (axis 0), we specify axis=0 in sum.
#axis = n -> reduce nth dimension
print(A.shape)
print(A.sum(axis = 0).shape)
print(A.sum(axis = 0))
print(A.sum(axis = 1).shape)
print(A.sum(axis = 1))
print(A.sum(axis = 2).shape)
print(A.sum(axis = 2))
print(A.sum(axis = [0, 1, 2]) == A.sum())

#mean value
print(A.mean())#all elements by default
print(A.sum()/A.numel())
#Likewise, the function for calculating the mean can also reduce a tensor along specific axes.
print(A.mean(axis = 0))
print(A.mean(axis = 1))
print(A.mean(axis = 2))
