import torch

x = torch.arange(12, dtype = torch.float32)
x.reshape(3,4)
#exp(x) elementwise
x = torch.exp(x)
print(x)

#binary scalar operators between u, v (in the same shape)
a = torch.tensor([1,2,4,8])
b = torch.tensor([2, 2, 2, 2])
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)

#concatenate two tensors
X = torch.arange(12, dtype=torch.float32)
X = X.reshape(3,4)
Y = torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])
print(X)
print(Y)
print(torch.cat((X,Y), dim = 0))
print(torch.cat((X,Y), dim = 1))

#logical statements
print(X==Y)
print(X > Y)

#summing all the elements
print(X.sum())
print(Y.sum())
