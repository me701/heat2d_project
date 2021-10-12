"""
# Do this or add /path/to/heat2d_project to your PYTHONPATH env. var.
import sys
sys.path.append('/Users/robertsj/heat2d_project/')
"""

"""
Refrigerator 

Consider a typical dorm-room-esque fridge with a square 0.5 m x 0.5 m outer 
dimension.  In 2-D, the height is "infinite", but for consistent
units, we can assume it's 1 m.  

We'll suppose in the back is a small rectangle that represents our 
heat sink (the pump-driven heat exchanger that actively removes heat).  

Here's a schematic

  <-- 0.5 m ---------->
  =====================
  |                   |     The outer walls are defaulted to 0.01 m thick
  |                   |     and consist of styrofoam (k = 0.033 W/m K).
  |                   |
  |               --- |     The heat sink is 0.2 m by 0.1 m.  It is centered
  |               |q| |     in the fridge along one axis, and it sits 0.05 m
  |               |q| |     from the nearest wall.  By default, assume
  |               --- |     that the heat sink removes 30 W and take its
  |                   |     conductivity to be 70 W/m K.
  |                   |     
  |                   |     Assume the fridge is approximately
  =====================     completely filled with a fine, fermented, barley
                            beverage, so, k = 0.6 W/m K.
                            
Finally, assume the exterior temperature at all four sides is a comfortable 
room temperature, or 20 C.     
                          
"""

from heat2d import solve

import numpy as np
  
x = np.linspace(0.0, 0.5, 100)
y = np.linspace(0.0, 0.5, 100)

def k(x,y):
    return 1.0

def q(x,y):
    return 0.0

boundaries = [20.0, 20.0, 20.0, 20.0]

T = solve(x, y, k, q, boundaries, plot=True, save=True)


