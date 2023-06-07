import torch

#commonly we want to sum up the gradients of each component of y with respect to the full vector x
#yielding a vector of the same shape as x.
#For example, we often have a vector representing the value of our loss function calculated separately for each example among a batch of training examples.
#Here, we just want to sum up the gradients computed individually for each example.


#PyTorch takes some steps to avoid confusion. Invoking backward on a non-scalar elicits an error unless we tell PyTorch how to reduce the object to a scalar.
x = torch.arange(4.0)
y = x * x
y.backward(gradient=torch.ones(len(y))) #or y.sum().backward()
print(x.grad)