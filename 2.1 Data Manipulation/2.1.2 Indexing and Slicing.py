import torch

x = torch.arange(12, dtype = torch.float32)
print(x)
x = x.reshape(3,4)
print(x)
#x[-1] selects the last row
print(x[-1])
#x[1:3] selects the 1st and the 2nd row
print(x[1:3])

#write elements
x[1,2] = 999
print(x)

#assign multiple elements
x[:2, 2] = 999
print(x)
x[:, 3] = 111
print(x)