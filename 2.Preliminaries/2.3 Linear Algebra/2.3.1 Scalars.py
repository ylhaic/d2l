import torch
#the expression x ∈ R is a formal way to say that x is a real- valued scalar.
#Scalars are implemented as tensors that contain only one element.

x = torch.tensor(3.0)
y = torch.tensor(2.0)
print(x+y, x*y, x/y, x**y)