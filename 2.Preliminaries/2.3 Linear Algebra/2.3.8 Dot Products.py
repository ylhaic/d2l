import numpy
import torch

#sum over the products of the elements at the same position
x = torch.arange(3, dtype = torch.float32)
y = torch.ones(3, dtype = torch.float32)

print(x)
print(y)
print(x * y)
print(torch.sum(x * y))


A = torch.tensor([[5,4,2],[3,7,1],[8,0,9]])
B = torch.tensor([[2,8,9],[1,6,7],[5,0,4]])
print(torch.sum(A * B))