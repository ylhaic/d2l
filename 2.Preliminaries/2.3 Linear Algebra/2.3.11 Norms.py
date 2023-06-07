import torch

#The Euclidean norm that we all learned in elementary school geometry
#when calculating the hypotenuse of right triangle is the square root of the sum of squares of a vector’s elements.
u = torch.tensor([5.0, 12.0])
print(torch.norm(u))
#length of the vector

#The l1 norm is also popular and the associated metric is called the Manhattan distance.
#By definition, the l1 norm sums the absolute values of a vector’s elements
print(torch.abs(u))
print(torch.abs(u).sum())