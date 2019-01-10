'''
This module is for reading and manipulating
strings of data coming in or feeded offline

Data streaming from Kinect:
    I will use the freenect driver with python wrapper
    to access the data streaming from Kinect sensor.
    For python environment I build the libfreenect driver
    using cmake and make

    I encapsulate the use of freenect inside a python environment
    using python 2.7 
    Other packages required for this data streaming is mayavi, numpy,
    and if necessary sympy for visualization, computation, symbolic solution (if
    necessary)

    If the freenect driver would not work, I can copy the contents of the 
    lib and bin directories in the built freenect into the lib and bin directories
    in the python environment (~/anaconda3/envs/my_environment/[bin,lib] etc)

    For a virtual environment, I suggest installing mayavi after it is generated using
    pip instead of installing using conda to avoid incompatibility with vtk packages
    dependent on the mayavi package
'''
import freenect, cv2
import numpy as np
import sympy as sym


