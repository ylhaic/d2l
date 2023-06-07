import numpy as np
from matplotlib_inline import backend_inline
from d2l import torch as d2l

#define f(x) = 3x^2 - 4x
def f(x):
    return 3 * x ** 2 - 4 * x

#set x = 1, f'(x) approaches 2 as h approaches 0
for h in 10.0 ** np.arange(-1, -6, -1):
    print(f'h = {h:.5f}, numerical limit={(f(1+h) - f(1))/h:.5f}')