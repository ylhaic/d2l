import torch
import numpy

X = torch.tensor([[0,1],[2,3]])
A = X.numpy()
B = torch.from_numpy(A)
print(type(X), type(A), type(B))

a = torch.tensor([3.5])
print(a, a.item(), float(a), int(a))