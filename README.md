# ME 701 - Project 1


## Description

For this project, your team (of $\leq 3$ students) will adapt the open-source 
code in `fd2d_heat_steady.py` to produce an easy-to-use program
for modeling 2-d heat conduction.  Because the numerical methods needed
are completely implemented in the given code, the challenges for your team
are (1) to understand how the existing code works and (2) to craft a new 
interface that takes a given "input" and provides a desired "output."  You 
are free to change code in `fd2d_heat_steady.py`, or you may import only 
those pieces you want or need.  You should *avoid* simply copying code from
`fd2d_heat_steady.py` into new functions that do basically the same thing.

## What You are Given

This project repository contains several files that define your path 
forward:

  - `heat2d/fd2d_heat_steady.py` is the same file we saw earlier in class (unmodified
     from its [original source](https://people.sc.fsu.edu/~jburkardt/py_src/fd2d_heat_steady/fd2d_heat_steady.html) 
     as of 10/12/2021.
     
  - `heat2d/__init__.py` is used to perform imports and other operations
     needed to set up the module.  In particular, this imports the `solve`
     function defined in driver.
     
  - `heat2d/driver.py` defines the `solve` function and the `plot`
     function.
  
  - `examples/simple_box.py` defines a very simple, 2-d heat conduction
     problem without any heat sources.  This is equivalent to the 
     example given in `fd2d_heat_steady.py`.  However, note that
     the inputs to `solve` differ from the `fd2d_heat_steady` function
     defined in `fd2d_heat_steady.py`.
     
  - `examples/simple_box_ref.png` is identical to the image that should be 
     produced by `heat2d.plot`.
     
  - `examples/simple_box_ref.out` is identical to the text-based output
     that should be saved to file.  Hint: `np.savetxt` is your friend. 
     
  - `examples/refrigerator.py` defines a more realistic application.  
     Although refrigeration units rely on convection for removing
     heat, we can approximate the heat exchanger with a fixed, *negative*
     heat source.  

## Tasks

  - Fully implement the `solve` and `plot` functions.  You may add 
    additional functions to the `driver.py` module as needed.  All development
    should be *clearly* shown in `git` logs.  Development should include
    multiple pull-request and review cycles.
    
  - Run the code to produce `simple_box.png` and `simple_box.out`.
    
  - Implement the `q` and `k` functions needed for the refrigerator 
    "default" example.  Run and save your `png` and `out` files.  
    Note the temperatures within the refrigerator region.
    
  - Create a Jupyter notebook that demonstrates your tool by "optimizing" the 
    refrigerator materials or heat sink to
    ensure the minimum temperature inside the refrigerator is equal to 
    or below 4 $^{\circle}$ C.  Show the results first for the "default" 
    configuration.  Then describe your optimization process and the
    final "design."  Compare your results to real fridges; are
    they even remotely comparable?
    
    Warnings:
    
      - The "default" fridge geometry has 1 cm-thick walls.  Hence, please
        don't divide the 50 cm of space into 11 or 21 or whatever cells.  
        Make sure you use a grid that can actually capture the geometry!
      - You may wish to test how sensitive things like "minimum temperature"
        are to the "delta" used to discretize the domain.
      - As "delta" gets small, the matrix gets big.  
    
## Deliverable

  - Your group repository must contain all of the files and output noted
    above.  Your Jupyter notebook should be committed in an "executed"
    state, i.e., all your results should be visible from GitHub.
    
    
    
  
    
  


