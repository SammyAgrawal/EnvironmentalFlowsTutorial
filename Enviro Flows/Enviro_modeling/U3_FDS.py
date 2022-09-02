# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

## Define variables that do not change for different grids
L = 3 # length of domain
m = 0 # counter for number of grid sizes to plot


## Loop over different grid sizes (N = number of points in domain)
N = np.array([8, 16, 32, 64, 128, 256, 512, 1024, 2048]) 
dx = np.empty(9)
error_1st = np.empty(9)
error_2nd = np.empty(9)
error_4th = np.empty(9)

for i in np.nditer(N):    
    # Define resolution-dependent variables
    deltax = L/i                       # grid spacing
    x = np.linspace(0,L,i)          # define x and grid
    nx = len(x)                        # number of points in grid
    
    f = np.sin(5*x)                    # set f to function to be differentiated
    
    dfdx_exact = 5*np.cos(5*x)         # exact (analytical) derivative
    
    # Initialize arrays for 3 schemes with NaNs so that un-used values at the edge of the domain will not be plotted. 
    # This isn't necessary, but just makes the plotting a bit easier.
    dfdx_1st = np.nan*np.ones(len(dfdx_exact))
    dfdx_2nd = np.nan*np.ones(len(dfdx_exact))
    dfdx_4th = np.nan*np.ones(len(dfdx_exact))
    
    # Compute derivatives with three different approximations
    for j in range(3,nx-2): 
        dfdx_1st[j] =  (f[j+1]-f[j])/deltax                           # first order forward
        # TO DO: second order central
        # TO DO: fourth order central
    
       
    # TO DO: Plot the exact and approximated derivatives for the case where N=16

    
    # Extract the errors for x = 1.5, the midpoint of the domain
    dx[m] = deltax         # store the current deltax in an array for plotting later
    midpoint = int(i/2-1)  # calculate the midpoint index 
    
    error_1st[m] = abs(dfdx_1st[midpoint]-dfdx_exact[midpoint])
    error_2nd[m] = abs(dfdx_2nd[midpoint]-dfdx_exact[midpoint])
    error_4th[m] = abs(dfdx_4th[midpoint]-dfdx_exact[midpoint])
    
    
    m = m+1  # advance counter for number of grids




## TO DO: Plot dx versus error at x = 1.5

