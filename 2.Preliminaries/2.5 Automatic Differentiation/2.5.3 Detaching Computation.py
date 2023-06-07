#Sometimes, we wish to move some calculations outside of the recorded computational graph.
#suppose wehavez = x * yandy = x * xbutwewanttofocusonthedirectinfluenceofxon z rather than the influence conveyed via y
#In this case, we can create a new variable u that takes the same value as y
#but whose provenance (how it was created) has been wiped out.

import torch

x = torch.arange(4.0)
x.requires_grad_(True)
y = x * x
print(y)
u = y.detach()
z = u * x

z.sum().backward()
print(x.grad == u)