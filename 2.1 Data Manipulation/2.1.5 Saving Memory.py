import torch

X = torch.tensor([[0,1],[2,3],[4,5]])
Y = torch.tensor([[5,4],[3,2],[1,0]])

before = id(Y)
Y =  Y + X
print(id(Y) == before)
#1.save memory 2.we might reuse values
Z = torch.zeros_like(Y)
print('id(Z): ', id(Z))
Z = X + Y
print('id(Z): ', id(Z))

before = id(X)
X += Y
print(id(X) == before)