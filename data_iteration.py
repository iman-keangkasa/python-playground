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
    
    TO DO:

    [X] I also will include a Hokuyo driver and its c++ driver wrapper. Please look into this
'''
import freenect, cv2
import numpy as np
import sympy as sym
#from kinect_test import *
from calibkinect import depth2xyzuv
from mayavi import mlab
import pptk


#def cv_visual():
#    '''
#    use kinect_test to show the visual
#    from kinect_test
#    
#    while 1:
#        #get a frame from RGB camera
#        frame = get_video()
#        #get a frame from depth sensor
#        depth = get_depth()
#        #display RGB image
#        cv2.imshow('RGB image',frame)
#        #display depth image
#        cv2.imshow('Depth image',depth)
#
#        # quit program when 'esc' key is pressed
#        k = cv2.waitKey(5) & 0xFF        if k == 27:
#            break
#    cv2.destroyAllWindows()
#    '''
#    
#    while 1:
#        #get a frame from RGB camera
#        frame = get_video()
#        #get a frame from depth sensor
#        depth = get_depth()
#        #display RGB image
#        cv3.imshow('RGB image',frame)
#        #display depth image
#        cv2.imshow('Depth image',depth)
#
#        # quit program when 'esc' key is pressed
#        k = cv2.waitKey(5) & 0xFF 
#        if k == 27:
#            break
#    cv2.destroyAllWindows()
#
#def raw_depth():
#    '''
#    get the raw depth data
#    from the kinect using the kinect_test
#    '''
#    return get_depth()

def point_cloud():
    '''
    turn depth into raw data
    '''
    return depth2xyzuv(freenect.sync_get_depth()[0])

#attempting visualization FAIL
#DO NOT USE mlab DIRECTLY WITH
#RAW POINT CLOUDS

#def point_cloud_visual():
#    '''
#    Attempting visualization using mlab. just a screenshot [1 Feb 2019]
#    DO NOT USE THIS METHOD
#    '''
#    xyz, uv = point_cloud()
#    s = mlab.points3d(xyz[:,0],xyz[:,1],xyz[:,2])
#    mlab.show()

def pptk_point_cloud_visual(reload=False):
    '''
    Using PPTK package to visualize
    point cloud directly
    
    use pptk.load(xyz) to reload the 
    viewer with new set of point cloud
    
    To reload, set argument reload=True
    '''
    if reload:
        xyz, uv = point_cloud()
        v.load(xyz)
    else:
        xyz, uv = point_cloud()
        v = pptk.viewer(xyz)
    return v
def pptk_reload(v=pptk_point_cloud_visual()):
    '''
    Reload the point cloud
    in a pptk viewer
    '''
    v.clear()
    v.load(point_cloud()[0])


