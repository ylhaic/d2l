import torch

#We can think of the matrix-matrix multiplication AB as performing m matrix-vector products
#or m × n dot products and stitching the results together to form an n × m matrix.
#In the following snippet, we perform matrix multiplication on A and B.
#Here, A is a matrix with 2 rows and 3 columns, and B is a matrix with 3 rows and 4 columns.
#After multiplication, we obtain a matrix with 2 rows and 4 columns.

A = torch.arange(6, dtype = torch.float32).reshape(2, 3)
B = torch.arange(12, dtype = torch.float32).reshape(3, 4)

print(torch.mm(A, B))
print(A@B)