'''
This module contains numpy's
classes to do numerical methods

TODO:
    [x] numerical comparison --- find a way to
    construct a truth table that can be access
    using index 
        [solution] This usually comes with QUESTIONS 
        np functions (all, any, nonzero, where)
        the output(in tuples) is not scriptable.

        However we need to np.transpose(the_output)
        so that the tuples become indexable
        the first column would be the row values
    [ ] Look into structured array: Using string
        in array indexing (structured datatype)
    [ ] Linear Algebra
    [ ] Prob. and statistic
10/12/2018
Stop at Linear Algebra

'''
from numpy import array, arange, linspace, sin, hstack,vstack, transpose, where

def reshape_it(the_array,dimensions):
    '''
    To reshape the array into
    different shape (dimension/axis)
    syntax:
    the_array is a numpy array object
    dimension_spec is a list containing
    the shape of the array

    to do
    a= a.reshape(row,col)
    we can also do this:
    a.shape = (row,col)
    '''
    size = 1
    #find if dimension given is valid
    for axis in dimension_spec:
        size *= axis
    if size == the_array.size:
        return the_array.reshape(*dimensions)

def creates_steps_array(dimensions,start,finish, steps):
    '''
    This function create an
    array with equal steps
    np.arange() is used
    
    np.arange(start,finish,steps)
    (remember that python has an offset by 1)

    syntax:
    creates_line_array(dimensions,start,finish,steps)
    
    dimension: a list describing the shape
    start: the starting of line
    finish: the termination of the line off by 1
    steps: the increment for each interval
    
    '''
    a=arange(start,finish,steps)
    dim_check = 1
    for axis in dimensions:
        dim_check *= axis
    
    if dim_check == a.size:
        return a.reshape(*dimensions)
    else:
        print("The dimension does not match the line-space")
        print("Try dimension that multiplies to:{}".format(a.size))
def linspace_it(start,finish,points):
    '''
    This function uses np.linspace()
    start is a starting point
    finish is a termination point (not off by one)
    points is the number of points between start and finish
    '''
    return linspace(start,finish,points)

def linspace_sin(points):
    '''
    linspace_sin receive an array that has 
    been generated using linspace_it() function
    which uses np.linspace() function
    '''

    return sin(points)

def array_resize(an_array,row,col):
    '''
    In this function, I invoke
    the resize(*dimensions) of a
    numpy object.

    This function is different
    from reshape because
    the array is changed permanently
    '''
    an_array.resize(row,col)

def numerical_comparison(the_array,compare,this_number,output_type='index'):
    '''
    Comparison with a numpy object
    is
    array < a_number
    array > a_number
    array <= a_number
    array >= a_number
    array == a_number
    
    The function would return an array of
    the form [ [row,col] ] ... of the
    location where the condition is true
    
    a_zero
    array([[0., 1., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])

    indices3 = np.transpose(np.where(a_zero == 1))
    
    indices3
    array([[0, 1],
           [1, 1],
           [2, 2]])

    '''
    if output_type == 'index':
        if compare == '<':
            return np.transpose(np.where(the_array < this_number))
        if compare == '>':
            return np.transpose(np.where(the_array > this_number))
        if compare == '<=':
            return np.transpose(np.where(the_array <= this_number))
        if compare == '>=':
            return np.transpose(np.where(the_array >= this_number))
        if compare == '==':
            return np.transpose(np.where(the_array == this_number))
        if compare == '!=':
            return np.transpose(np.where(the_array != this_number))

    else:
        if compare == '<':
            return the_array < this_number
        if compare == '>':
            return the_array > this_number
        if compare == '<=':
            return the_array <= this_number
        if compare == '>=':
            return the_array >= this_number
        if compare == '==':
            return the_array == this_number
        if compare == '!=':
            return the_array != this_number


def basic_operation():
    '''
    In numpy multiplication using *, -, +,
    is elementwise

    The matrix product uses the @ operator

    The method in each numpy array:
    .sum(axis=a) a takes 0 until the largest_dim - 1
    .min(axis=a)
    .max(axis=a)
    .cumsum(axis=a) add the total to the last element in the array
    b =
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    
    b.cumsum(axis=1)
    array([[ 0,  1,  3,  6],
           [ 4,  9, 15, 22],
           [ 8, 17, 27, 38]])
    
    result = np.exp(b) will get the exponential
    '''
def array_slicing():
    '''
    One-dimensional arrays can be indexed, sliced and iterated over, 
    much like lists and other Python sequences.

    a = np.arange(10)**3
    array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
    
    a[2]
    8
    
    a[2:5]
    array([ 8, 27, 64])
    
    From start to position 6, exclusive, set every 2nd element to -1000:
    a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; 
    a
    array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
    
    Reverse a:
    a[ : :-1] 
    array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
    
    For multi-dimensional array
    
    I can generate a multidimensional
    array from a function
    say:

    f = lambda x,y: 10*x+y
    b = np.fromfunction(f, (5,4), dtype=int)
    b
    array([[ 0,  1,  2,  3],
           [10, 11, 12, 13],
           [20, 21, 22, 23],
           [30, 31, 32, 33],
           [40, 41, 42, 43]])
    
    b[2,3]
    23

    b[0:5,1]
    array([ 1, 11, 21, 31, 41])
    
    b[ : ,1]                        # equivalent to the previous example
    array([ 1, 11, 21, 31, 41])
    
    b[1:3, : ]                      # each column in the second and third row of b
    array([[10, 11, 12, 13],
           [20, 21, 22, 23]])
    
    When fewer indices are provided than the number of axes, 
    the missing indices are considered complete slices:
    
    b[-1]                                  # the last row. Equivalent to b[-1,:]
    array([40, 41, 42, 43])

    The dots (...) represent as many colons as needed 
    to produce a complete indexing tuple. 
    For example, if x is an array with 5 axes, then

    x[1,2,...] is equivalent to x[1,2,:,:,:],
    x[...,3] to x[:,:,:,:,3] and
    x[4,...,5,:] to x[4,:,:,5,:].

    c = np.array( [[[  0,  1,  2],              
                    [ 10, 12, 13]],
                   [[100,101,102],
                    [110,112,113]]])
    c.shape
    (2, 2, 3)
    
    c[1,...]                                   # same as c[1,:,:] or c[1]
    array([[100, 101, 102],
           [110, 112, 113]])
    
    c[...,2]                                   # same as c[:,:,2]
    array([[  2,  13],
           [102, 113]])

    To iterate over a multi-dimensional array:

    for element in b.flat"
        print(element)

    is equivalent to:
    
    for row in b:
        for element in row:
            print(element)

    '''
def stacking_arrays(a,b,direction):
    '''
    stacking can be done using np.hstack,np.vstack
    or using np.column_stack.

    The arrays must be encapsulated with a ()
    np.column_stack((a,b))

    The np.newaxis can be use to turn
    a one dimensional array 
    one_dim = np.array([1,2,3]) which has (3,) shape
    into a two dimensional array
    one_dim[:,np.newaxis]

    np.concatenate can also be used to stack arrays
    however I must specify the direction using axis
    flag. If axis = None is specify, the concatenation will
    resolve into a 1D array
    '''
    if direction == 'horizontal':
        if a.shape[0] == b.shape[0]:
            return hstack((a,b))
        else:
            print("The row does not match")
    if direction == 'vertical':
        if a.shape[1] == b.shape[1]:
            return vstack((a,b))
        else:
            print("The column does not match")

def shallow_copy():
    '''
    Different array objects can share 
    the same data. The view method creates
    a new array object that looks at 
    the same data

    c = a.view()
    
    c.flags.owndata
        ---> False
    c.base is a
        ---> True
    
    The shape of c is independent of a and vice versa
    However, even after the shape of c changes, the assignment
    of values in c will change the corresponding
    value in a.

    shallow copy also applies to slicing using
    the operator ':'


    '''

def deep_copy():
    '''
    deep copy is severed any interaction between
    the original array and the copy array

    Changes in on will not affects the other.
    '''

def numpy_functions():
    '''
    ARRAY CREATION
    arange, array, copy, empty, empty_like, eye, fromfile, 
    fromfunction, identity, linspace, logspace, mgrid, 
    ogrid, ones, ones_like, r, zeros, zeros_like
        
    CONVERSION
    ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
    
    MANIPULATION
    array_split, column_stack, concatenate, diagonal, dsplit, 
    dstack, hsplit, hstack, ndarray.item, newaxis, ravel, 
    repeat, reshape, resize, squeeze, swapaxes, take, 
    transpose, vsplit, vstack
    
    QUESTION
    all, any, nonzero, where
    
    ORDERING
    argmax, argmin, argsort, max, min, ptp, searchsorted, sort
                        
    OPERATION
    choose, compress, cumprod, cumsum, inner, 
    ndarray.fill, imag, prod, put, putmask, 
    real, sum
      
    BASIC STATISTICS
    cov, mean, std, var
    
    BASIC LINEAR ALGEBRA
    cross, dot, outer, linalg.svd, vdot 
    '''

