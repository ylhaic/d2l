import torch

a = torch.arange(3).reshape((3,1))
b = torch.arange(2).reshape((1,2))
print(a)
print(b)
#a is a 3*1 matrix, b is a 1*2 matrix
#a+b expands a and b to 3*2
#a' = tensor([[0,0],[1,1],[2,2]])
#b' = tensor([[0,1],[0,1],[0,1]])
print(a+b)

X = torch.arange(4).reshape((1,4))
Y = torch.arange(8).reshape((8,1))
Z = torch.arange(2).reshape((1,2))
print(X+Y)
print(Y+Z)

x = torch.arange(27).reshape((3,3,3))
y = torch.arange(3).reshape((1,1,3))
print(x)
print(y)
print(x+y)