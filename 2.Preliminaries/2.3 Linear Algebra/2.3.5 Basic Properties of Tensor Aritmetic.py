import torch
#elementwise summation
A = torch.arange(6, dtype = torch.float32).reshape(2, 3)
B = A.clone()
print(A)
print(A+B)
#elementwise product
print(A*B)
#Adding or multiplying a scalar and a tensor produces a result
#with the same shape as the original tensor.
#Here, each element of the tensor is added to (or multiplied by) the scalar.
a = 2
C = torch.arange(24).reshape(2,3,4)
print(a + C)
print((a * C).shape)