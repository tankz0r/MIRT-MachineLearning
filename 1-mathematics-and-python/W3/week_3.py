from __future__ import division
from scipy.optimize import minimize
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import differential_evolution
import pdb

def f(x):
    f=np.sin(x/5)*np.exp(x/10)+5*np.exp(-x/2)
    return f

def h(x):
    h=int(f(x))
    return h
"""
x0 = (30)
res = minimize(h, x0, method='BFGS')
print res

"""
bounds = [(1, 30)]
res = differential_evolution(h, bounds)
print res

#pdb.set_trace()
