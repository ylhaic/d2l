#you can think of vectors as fixed-length arrays of scalars.
#We denote vectors by bold lowercase letters, (e.g., x, y, and z)
#Vectors are implemented as 1st-order tensors.
#in Python, like in most programming lan- guages, vector indices start at 0
#also known as zero-based indexing, whereas in linear algebra subscripts begin at 1
import torch

x = torch.arange(5)
print(x)
print(x[2])#scalar

#To indicate that a vector contains n elements
#we write x ∈ Rn. Formally, we call n the dimensionality of the vector.
#In code, this corresponds to the tensor’s length
#accessible via Python’s built-in len function.
print(len(x))
#To indicate that a vector contains n elements
#we write x ∈ Rn. Formally, we call n the dimensionality of the vector
#In code, this corresponds to the tensor’s length
#accessible via Python’s built-in len function.
print(x.shape)

