#As we pass data through each successive function
#the framework builds a computational graph that tracks how each value depends on others
#To calculate derivatives, automatic differentiation works backwards through this graph applying the chain rule.
#The computational algorithm for applying the chain rule in this fashion is called backpropagation.

import torch

#create a place to store the gradient of y w.r.t. x
x = torch.arange(4.0)
print(x)
x.requires_grad_(True)
""""same as x = torch.arange(4.0, requires_grad=True)"""
x.grad #the gradient is None by default

#calculate our function of x and assign the result to y
y = 2 * torch.dot(x, x)
print(y)

#We can now take the gradient of y w.r.t. x by calling its backward method
#Next, we can access the gradient via x’s grad attribute.
y.backward()
print(x.grad)

#gradient of y = 2 x^T x is 4 x
print(x.grad == 4 * x)



#another function
x.grad.zero_() #reset the gradient
y = x.sum()
print(y)
y.backward()
print(x.grad)