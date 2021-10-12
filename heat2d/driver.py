from . import fd2d_heat_steady


def solve(x, y, k, q, b, plot=False, save=False):
    """Solve the conduction problem given materials, sources, and 
       boundary temperatures.
       
       `x` and `y` are NumPy arrays that define the divisions along
       either axis used to discretize the problem domain into a grid.
       
       `k` and `q` are functions of `x` and `y` that return the  
       conductivity (W/m-K) or heat-generation rate (W/m^3-s) at a given
       location.
       
       `b` is an array of four values that indicate the left, right,
       bottom, and upper temperatures of the 2-d domain.
       
       If a plot of the solution is desired, `plot` should be set
       to the filename of the plot.
       
       If the temperatures are to be saved to a text file, `save` should be
       set to the filename of the text file.
       
       Returns the temperature as a two-dimensional array with the same
       dimensions as `k` and `q`.
    """
    
    raise NotImplemented # <-- remove this!
    
