'''
Integrate.py 

Uses the trapezium rule to integrate a given function, defined before the
program runs.
'''

# - - - Import Statements - - -

import numpy as np

# - - - Global Variables - - -

BINS = 100  # the number of bins to use in the integration
START = 0  # value to integrate from
END = 50  # value to integrate to

# - - - Function Definitions - - -


def func(x):
    '''
    The function to be integrated, best to define using numpy routines.

    Args:
    x (float): the input variable

    Returns:
    y (float): value of the function when evaluated for x
    '''
    y = x**2  # Define the function here
    return y


def func_2(x):

    y = 1/x
    return y


def trapezium(a, b, h):
    '''
    Calculates the area of a trapezium of parallel side lengths a,b, and 
    'height' h. NB: in the context of the trapezium method of integration, 
    height is actually the width.

    Important: negative areas ARE possible here - this is due to the context
    of integration.

    Args:
    a (float): the length of one parallel side
    b (float): the length of the other parallel side
    h (float): the height (not always height) of the trapezium

    Returns:
    area (float): the area of the trapezium
    '''
    return h*(a+b)/2


def integrate(f, start, end, bins, density):
    '''
    Integrates the given function using the trapezium rule from start to finish
    over 'bins' trapezia.

    Args:
    f (func): function to be integrated
    start (float): value to integrate from
    end (float): value to integrate to
    bins (int): number of trapezia to use

    Returns:
    area (float): estimated area under the curve
    '''
    area = 0
    edges = np.linspace(start, end, bins)
    bin_width = (end - start)/bins
    for i in range(len(edges)-1):
        y1 = f(edges[i])*density
        y2 = f(edges[i+1])*density
        trp_area = trapezium(y1, y2, bin_width)
        area += trp_area
    return area

# - - - Main Code - - -


DENSITY = [13000, 7000, 5000, 3900, 2835]
DEPTHS = [13e-16, 1365, 3602, 5848, 6217, 6250]
int_1 = integrate(func, DEPTHS[0], DEPTHS[1], BINS, DENSITY[0])
int_2 = integrate(func, DEPTHS[1], DEPTHS[2], BINS, DENSITY[1])
int_3 = integrate(func, DEPTHS[2], DEPTHS[3], BINS, DENSITY[2])
int_4 = integrate(func, DEPTHS[3], DEPTHS[4], BINS, DENSITY[3])
int_5 = integrate(func, DEPTHS[4], DEPTHS[5], BINS, DENSITY[4])


final_val = 48*np.pi*np.pi/5 * \
    integrate(func_2, DEPTHS[0], DEPTHS[5], BINS *
              6, (int_1+int_2+int_3+int_4+int_5))
print(f"total Binding energy= {final_val:.3g}.")
