import numpy as np
from matplotlib_inline import backend_inline
from d2l import torch as d2l

def f(x):
    return 3 * x ** 2 - 4 * x

def use_svg_display():  #@save
    """use the svg format to display a plot in Jupyter"""
    backend_inline.set_matplotlib_formats('svg')

def set_figsize(figsize = (3.5, 2.5)):  #@save
    """set the figure size for matplotlab"""
    use_svg_display()
    d2l.plt.rcParams['figure.figsize'] = figsize

def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):  #@save
    """set the axes for matplotlab"""
    axes.set_xlabel(xlabel), axes.set_ylabel(ylabel)
    axes.set_xscale(xscale), axes.set_yscale(yscale)
    axes.set_xlim(xlim), axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()

#With these three functions, we can define a plot function to overlay multiple curves.

#@save
def plot(X, Y = None, xlabel = None, ylabel = None, legend = [],
         xlim = None, ylim = None, xscale = 'linear', yscale = 'linear',
         fmts = ('-', 'm--', 'g-.', 'r:'), figsize = (3.5, 2.5), axes = None):
    """plot data points"""
    def has_one_axes(X): # # True if X (tensor or list) has 1 axis
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list) and not hasattr(X[0], "__len__"))

    if has_one_axes(X):
        X = [X]
    if Y is None:
        X, Y = [[]] * len(X), X
    elif has_one_axes(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)

    set_figsize(figsize)
    if axes is None:
        axes = d2l.plt.gca()
    axes.cla()
    for x, y, fmt in zip(X, Y, fmts):
        axes.plot(x, y, fmt) if len(x) else axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)

x = np.arange(0, 3, 0.1)
plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])