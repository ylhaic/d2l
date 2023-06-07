#We denote general tensors by capital letters
#with a special font face (e.g., X, Y, and Z)
#and their indexing mechanism follows naturally from that of matrices.
import torch

A = torch.arange(24).reshape(2,3,4)
print(A)
print(A.shape)
print(len(A))