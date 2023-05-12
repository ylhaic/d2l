import torch
#create a vector of evenly spaced values
#starting at 0, ending at n (not included)
x = torch.arange(12, dtype=torch.float32)
print(x)

#.numel(), number of elements
print(x.numel())

#the length along each sides
print(x.shape)

#reshape
X=x.reshape(3,4)
print(X)
print(X.shape)
XX=x.reshape(6,2)
print(XX)
print(XX.shape)
#computer computes another value
#if one is specified and another one is -1
XXX=x.reshape(2,-1)
print(XXX)
print(XXX.shape)

#tensors initialised with all 0's or 1's
y = torch.zeros(3,3)
print(y)
yy = torch.ones(3,3)
print(yy)
yyy = torch.ones(2,3,4)
print(yyy)

#randomly initialise a tensor
#elements drawn from a
#standard Gaussian normal distribution
#with mean 0 and standard deviation 1
z = torch.randn(4,4)
print(z)