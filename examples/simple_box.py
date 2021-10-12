"""
# Do this or add /path/to/heat2d_project to your PYTHONPATH env. var.
import sys
sys.path.append('/Users/robertsj/heat2d_project/')
"""


from heat2d import solve

import numpy as np
  
x = np.linspace(0.0, 2.0, 21)
y = np.linspace(0.0, 1.0, 11)

def k(x,y):
    return 1.0

def q(x,y):
    return 0.0

boundaries = [10.0, 100.0, 0.0, 0.0]

T = solve(x, y, k, q, boundaries, plot=True, save=True)


