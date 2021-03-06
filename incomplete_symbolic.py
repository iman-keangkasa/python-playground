# coding=utf-8
'''
This module explains how to use
symbolic variables and the symbolic 
modules

TODO:
    for partial_decomp find a way to get the
    zeros and the roots for control application
    
    for partial_decomp find a way to isolate 
    each terms from the result

    get_terms function is not complete. Please look into it

    solve all function with keyword buggy

    create a function to find the root of a polynomial function

    Finish matrix part

Numerically, a very small value can 
be chopped off using chop=True flag 
in evalf() method
eva
'''

from sympy import symbols, expand, factor, init_printing, Eq, simplify, sympify, lambdify, collect, cancel, apart, trigsimp, expand_trig, powsimp, expand_power_exp, expand_power_base, powdenest, expand_log, logcombine, factorial, binomial, combsimp, diff, Derivative, solveset, linsolve, Matrix, nonlinsolve, sqrt, Lambda, Mod, ImageSet, FiniteSet, solve, roots, dsolve, zeros,eye, integrate, Integral, nonlinsolve, dsolve, Matrix, diag

def creates(lists):
    '''
    lists contains the names
    of variable you want to create
    symbolically
    
    syntax:
        a, b = sympy.symbols('a b') 
    
    this module will return a list of symbolic variables
    '''
    symbolic=[]
    for element in lists:
        #here element is a python variable
        # str(element) is a sympy symbolic variable
        element = symbols(str(element))
        symbolic.append(element)
    return symbolic

def expands(exprs):
    '''
    This is the syntax to expand an expression
    sympy.expand(exprs)
    '''
    return expand(exprs)

def substitutes_from_list(expression,variable_list):
    '''
    To substitute more than one variable
    in a single expression, I should use
    dictionary

    I could also use tuples
    '''
    
    #to get the list of variables
    varia = list(expression.free_symbols)
    variable_dict = dict(zip(varia,variable_list))
    
    return expression.subs(variable_dict)
    
def substitute_from_dict(expression, dictionary):
    return expression.subs(dictionary)
def beautiful_prints():
    '''
    This will start beautiful algebra
    for your workspace

    syntax:
    sympy.init_printing(use_unicode = True)
    '''
    init_printing(use_unicode = True)


def equates(a,b):
    '''
    create symbolic equalities
    The expression after Eq() is called will have 
    right-hand side
    left-hand side
    
    to separate expression = Eq(eq1,eq2)
    expression.lhs for left-hand side
    expression.rhs for right-hand side
    '''

    return Eq(a,b)


def equal_val(a,b):
    '''
    Test the similarity between two 
    expression
    Syntax:
    equal_val(a,b)

    The function uses a.equals(b) to 
    logically evaluate equality of
    a and b

    Returns bool value
    '''
    return a.equals(b)

def substitutes(a,sub1,sub2):
    '''
    This function will show how to
    do a simplification and substitute
    a function, sub1 into another function
    sub2 in a

    eg: cos(x)**2 + sin(x)**2 = 1
    sympy.expand_trig could not evaluate this
    '''
    return a.subs(sub1,sub2)

def substitutes_if(a,the_if):
    '''
    Substitute an expression with certain rules
    the_if is a comprehension list
    say

    the_if = [(x**i,y**i) for i in range(5) if i%2 == 0]
    '''
    return a.subs(the_if)
    

def str2sympy(a):
    '''
    Convert strings to sympy expression
    using
    sympy.sympify(a)
    where a is the string
    Syntax:
    v = str2sympy(a)
    '''
    return sympify(a) 

def floats(a,b={}):
    '''
    To change a value into
    a floating number use
    the method of the sympy object call evalf()

    say x is a sympy object
    x.evalf() 
    will give the floating value

    If a is an expression and b is a DICTIONARY
    to substitute the values into a
    it is more efficient to invoke the subs flag
    within evalf()
    syntax:
    result = x.evalf(subs={y:3})
    '''
    result = a.evalf(subs=b)

    return result

def sym2numeric(a):
    '''
    To do a large number of numerical method
    I should use numpy or math. Symbolic is 
    inefficient for that purpose.
    I should invoke sympy.lambdify
    Syntax:
    
    v=sympy.lambdify(x_variable,f_function, "numpy")

    If f_function has more than one variables,
    we should use a list of the variable:
    
    var_list = list(f_function.free_symbols)
    v = sympy.lambdify(var_list, f_function, "numpy")
    
    In sym2numeric, I am using a python concept call
    lambda. It is the closest of mathematical function
    equivalent in python 

    say I have f of x, f(x) = 2x + 3
    to generate the function f in python
    I can use lambda:
    f = lambda x: 2*x + 3
    f(3) = 9
    f(10) = 23
    '''
    var_list = list(a.free_symbols)
    numeric = lambdify(var_list, a, "numpy")
    return numeric

    
def create_function(func):
    '''
    This function creates a function where
    func is a string containing an expression
    of the function

    The pseudo-code:
    (1) convert func string into sympy expression
    (2) get the list of variables in func
    (3) lambdify the function 

    This is how I handle a string of expression into
    mathematical expression using the python lambda
    concept
    '''
    fsym = sympify(func)
    var_list = list(fsym.free_symbols)
    return lambdify(var_list, fsym, "numpy")

def latex_it(expression):
    '''
    This function gives out the latex
    equivalence of an expression
    It uses sympy.latex() 
    '''
    return latex(expression)

# SIMPLIFY FUNCTIONS #


def simplifies(a):
    '''
    using sympy.simplify(a)
    to simplify an expression
    
    sympy.simplify() uses heuristic approach 
    '''

    return simplify(a)

def expands(expression):
    '''
    The syntax is sympy.expand(a)
    '''
    
    if type(expression).__name__ == str:
        expression = sympify(expression)
        
    
    return expand(expression)

def factors(expression):
    '''
    If symplify fails, try factor()
    syntax:
    sympy.factor(expression)
    '''
    if type(expression).__name__ == str:
        expression = sympify(expression)

    return factor(expression)

def collects(expression):
    '''
    This function will rearrange the 
    expression according to the variables
    powers and factored out the coefficient.
    
    The expression MUST be expanded before hand.
    
    Collects CAN be used before coeff method of 
    an expression
    '''
    return collect(expression)

def get_coeff(expression,variable,order):
    '''
    coeff is a method for a sympy expression
    to get the coefficient of a variable
    of a certain order

    syntax:
    expression.coeff(variable,order)
    '''
    return expression.coeff(variable,order)

def cancels(expression):
    '''
    sympy.cancel() simplify a rational function into
    a canonical form p/q
    '''
    return cancel(expression)

def partial_decomp(expression):
    '''
    sympy.apart() will do partial fraction
    decomposition on a rational function
    '''
    return apart(expression)

# trigonometry #

def simple_trig_iden(expression):
    '''
    In sympy arc cosine or arc sine
    sympy.asin or sympy.acos respectively
    
    To simplify a trig function based on
    identities use:
    
    Can also be used with hyperbolic trig functions

    sympy.trigsimp()
    '''
    return trigsimp(expression)

def expands_trig(expression):
    '''
    Expand a trig function 
    Syntax:

    sympy.expand_trig(expression)
    '''
    return expand_trig(expression)

# powers #
def powers():
    '''
    Power functions in sympy has limitation.
    According to these identity:
    (1) x**a * x**b = x**a+b
    (2) x**a * y**a = (xy)**a
    (3) (x**a)**b = x**(ab)

    Identity (2) is only true when
    x and y are nonegative and a is real

    Identity (3) is true when 
    b is an integer
    
    sympy.powersimp() applies (1) and (2)
    from left to right. Simplifies an expression

    sympy.expand_power_exp() and sympy.expand_power_base() 
    applies identities (1) and (2). 
    
    expanse_power_base expand the power of base (eg x y)
    expanse_power_exp expand the power of the exponet (x**a)**b = x**(ab)
    
    sympy.powdenest() applies identity (3) from left to right
    '''
def simplifies_power(expression):
    '''
    Invoke identity (1) and (2)
    '''
    return powsimp(expression)    

def expands_power_base(expression):
    '''
    Invoke identity (1) and (2)
    The function expand the power of the
    base in the expression
    '''
    return expand_power_base(expression)

def expands_power_exp(expression):
    '''
    Invoke identity (1) and (2)
    The function expand the power of the
    exponent of the expression
    '''

def exponentials_logarithms():
    '''
    There are two identities:
    (1) log(x*y) = log(x) + log(y)
    (2) log(x**n) = n*log(x)

    Both requires x and y be real
    Both x and y should be positive
    and n should be real
    '''

def expands_log(expression):
    '''
    Uses sympy.expand_log() and
    applies identity (1) and (2)
    '''

    return expand_log(expression)

def combines_log(expression):
    '''
    Applies identities (1) and (2)
    
    This function uses sympy.logcombine() 
    to combine a log expression.
    '''
    return logcombine(expression)

def factorials(n):
    '''
    Represent the number of permutation
    of n distinct
    
    This function uses sympy.factorial(n)
    '''
    return factorial(n)

def binomials(n,k):
    '''
    Also noted as nCk,
    that says from n items choose k

    This function uses sympy.binomial()
    '''
    return binomial(n,k)

def rewrites(expression,interms):
    '''
    this function takes in sympy expression
    and invoke the rewrite method of
    the sympy expression(object) to rewrite
    it in terms of another function (interms)

    expression is sympy object
    interms is sympy object or string e.g: 'sin'
    '''
    return expression.rewrite(interms)

def calculus():
    '''
    DERIVATIVE:
    
    diff() --- as a function or a method
    Derivative() --- as a function
    
    Both compute the derivative but Derivative will
    not evaluate the expression (only show notation) before invoking
    the expression .doit() method
    '''

def diff_it(expression,respect_to, n=0, indefinite_n=False):
    '''
    this function uses diff in sympy
    to evaluate the derivative of an expression

    expression is a sympy object
    respect_to should be a list of how the derivative.
    '''
        
    if type(respect_to).__name__ == 'Symbol':
        if indefinite_n:
            n = symbols('n')
            print("Invoking indefinite n")
            return expression.diff(respect_to,n)
        else:
            print("Invoking single differentiation")
            return expression.diff(respect_to,n)

    if type(respect_to).__name__ == 'list':
        
        #create a string from respect_to and orders list n
        
        
        for index, element in enumerate(respect_to):
            expression = expression.diff(element)
        return expression


def integrates(expression,respect_to, lower=None, upper=None, definite= True):
    '''
    The integrates can be invoke as a function 
    or a method
    sympy.integrate(expression, (reference,lower_limit,upper_limit))
    or
    sympy.integrate(expression, reference)

    The Integral function is used to integrate the indef
    sympy.Integral( expression, (respect, lower_limit, upper_limit) )
    or
    sympy.Integral(expression, respect)

    Integral function will only evaluate the integration by invoking the
    doit() method.

    Syntax for integrates
    integrates(expression, respect_to, lower=None, upper=None, definite=True)
    '''
    
    if definite:
        if type(lower).__name__ == 'NoneType':
            return integrate(expression, respect_to)
        else:
            return integrate(expression, (respect_to,lower,upper))
    else:
        if type(lower).__name__ == 'NoneType':
            return Integral(expression, respect_to)
        else:
            return Integral(expression, (respect_to,lower,upper))
    
def limits():
    '''

    the function is invoke by either
    sympy.limit(expression, variable, limit, direction)
    direction takes in the value '+' or '-'
    
    sympy.Limit(expression, variable, limit, direction) 
    will not evaluate the limit until the doit() method
    is invoke
    '''

def series_():
    '''
    To compute the asymptotic series expansions of functions
    around a point we use sympy object method series() to
    a function or an expression
   
    Syntax:
    object.series(x, x0, n) where x0 is the point of interest
    n is the order of x**n 
    the default is x0=0 and n=6
     
    You would get a landau O(x**4) which says that
    terms greater than or equal to x**4 will be omitted.
    To remove the landau notation: 
    
    object.series(x,0,4).remove0()
    
    '''

def differentiates_finite():
    '''
    sympy.differentiate_finite() evaluate the finite
    difference 
    say. The syntax:

    f, g = symbols('f g', cls=Function)
    
    differentiate_finite(f(x)*g(x))
    '''

def approximates_derivative():
    '''
    Here we use step-size 1:
    
    f = sympy.Function('f')
    dfdx = f(x).diff(x)
    dfdx.as_finite_difference()
    
    To use arbitrary steps(possibly containing symbolic expression):

    f = Function('f')
    d2fdx2 = f(x).diff(x,2)
    h = Symbol('h')
    d2fdx2.as_finite_difference([-3*h,-h,2*h])

    '''
#SOLVER

def solveset_it(expression, solve_for, equals_to=0):
    '''
    Syntax for solveset:
    sympy.solveset(sympy.Eq(expression,equals_to, solve_for, domain=S.Complexes)
    or
    if expr = expression - equals_to:
    sympy.solveset(expr,solve_for,domain=S.Reals)
    
    or simply:
    sympy.solveset(expr,solve_for)
    '''
    if equals_to == 0:
        return solveset(expression,solve_for)
    else:
        return solveset(Eq(expression,equals_to),solve_for)

def solve_it(expression, solve_for):
    '''
    This function uses sympy.solve(expression,solve_for)
    it returns the solution and its multiplicity
    '''

    return solve(expression, solve_for)

def linsolve_it(system,solve_for,result_type='list'):
    '''
    This function use sympy.linsolve() to solve
    linear system of eqns
    Three forms we can use:
    (1) list of eqn:
        linsolve([x+y-2,x-2y-4],(x,y)]
    
    (2) Using sympy.Matrix()
        linsolve( sympy.Matrix(([1,1,-2],[1,-2,-4])), (x,y))
    
    (3) Using A*x = b form: 
    
        (carefull with this form b does not need to be inverted)
    
        M=sympy.Matrix(((1,1,-2),(1,-2,-4)))
        system = A, b = M[:,:-1], M[:,-1]
        linsolve(system, x, y, z)

        linsolve will give answers in the form
        of a set:
        {(-8/3,2/3)}

        where x = -8/3
        and   y = 2/3

    this function would return a list of solution

    buggy: not generalized for more than one variables
    '''
    sol =list( linsolve(system, solve_for) )
    solution_list = [ sol[0][0], sol[0][1] ]
    if result_type == 'list':
        
        return solution_list
    if result_type == 'dict':
       
        solution_dict = dict(zip(solve_for,solution_list))
        return solution_dict
    
   
    
def nonlinsolve_it(system,solve_for,result_type = 'list'):
    '''
    To solve nonlinear equations use sympy.nonlinsolve(system, variables)
    similar to sympy.linsolve
    
    For nonlinear system, an infinitely many solution means it
    has POSITIVE DIMENSIONAL SYSTEM

    buggy : not generalized for more than one unknown
    '''

    sol =list( nonlinsolve(system, solve_for) )
    solution_list = [ sol[0][0], sol[0][1] ]
    
    if result_type == 'list':
        
        return solution_list
    if result_type == 'dict':
       
        solution_dict = dict(zip(solve_for,solution_list))
        return solution_dict
    if result_type == 'raw':
        return nonlinsolve(system, solve_for)

def get_terms(expression,result_type='list'):
    '''
    this is an attempt to get the terms in
    a polynomial equations

    
    if result_type == 'list':
        terms=expression.args
        term_count = len(terms)
        for 

    still buggy
    '''

def dsolve_it(expression, function):
    '''
    dsolve uses a function generated from:
    f = sympy.symbols('f', cls=Function)
    f(x)
    or:
    f =sympy.Function('f')

    expression is a differential equation
    generated from:
    diffeq = sympy.Eq(f(x).diff(x),sin(x) )
    
    the solution would have C1 to Cn as the
    coefficient values which 
    
    '''
    return dsolve(expression, function)    

#  MATRIX  #

def how_to_matrix():
    '''
    to create 
    [1 -1]
    [3  4]
    [0  2]
    v = sympy.Matrix([[1, -1],[3,4],[0,2]])
    
    A list of elements is always considered a column vector
    but a list of elements encapsulate with [ ] is always
    considered as a row vector

    A matrix shape is retrieved by invoking its attribute shape
    v.shape
    
    To access a row or a column:
    v.row(0)
    v.co1(1)

    To access an element:
    v[1,2]
    v[2,2]

    To delete or insert a row or a column:
    v.row_del[0]
    v_insert = v.row_insert(0, sympy.Matrix([[x, x]])

    [x -x]
    [1 -1]
    [3  4]
    [0  2]

    v_insert = v.row_insert(1, sympy.Matrix([[x, x]])
    [1 -1]           [1 -1]
      <--[x -x]      [x -x]
    [3  4]           [3  4]
    [0  2]           [0  2]
    
    To get the basic operation 
    v+v
    v-v
    v**2
    v**-1 ---> will get the inverse of v
                if it exist
    
    To get the transpose of the
    matrix
    v.T

    To constructs the matrix I can use
    sympy.eye(3) results in a 3x3 identity matrix
    sympy.zeros(2,3) 
    sympy.ones(2,3)

    To create a diagonal matrix
    sympy.diag(1,2,3)
    [1 0 0]
    [0 2 0]
    [0 0 3]
    
    The arguments to diag can be either numbers or matrices. 
    A number is interpreted as a 1×1 matrix. 
    The matrices are stacked diagonally. 
    The remaining elements are filled with 0s.
    
    diag(-1, ones(2, 2), Matrix([5, 7, 5]))
     ⎡-1  0  0  0⎤ sympy.diag(-1)
     ⎢           ⎥
     ⎢0   1  1  0⎥ sympy.diag(sympy.ones(2,2)
     ⎢           ⎥
     ⎢0   1  1  0⎥
     ⎢           ⎥
     ⎢0   0  0  5⎥ sympy.diag(sympy.Matrix([5,7,5])
     ⎢           ⎥
     ⎢0   0  0  7⎥
     ⎢           ⎥
     ⎣0   0  0  5⎦



    To find the determinant we use det() method
    
    v.det()
    
    To get the row echelon form use the rref() method
    
    v.rref()

    The result has a reduced row achelon formed matrix,
    and the second is a tuple of indices of the pivot
    columns

    To get the nullspace of a matrix use nullspace() method
    
    v.nullspace()

    The result has a list of column vectors that span the
    nullspace of the matrix

    To get the columnspace of a matrix, use columspace() method 
    
    v.columnspace()

    The result returns a list of column vectors that span the
    columnspace of the matrix

    To get the eigenvalues of a matrix use eigenvals method
    
    v.eigenvals()
    
    The result returns a DICTIONARY of eigenvalues:algebraic multiplicity
    pairs (similar to the output of roots)
    
    To get the eigenvectors use the eigenvects() method.

    v.eigentvects()

    The result returns tuples within a tuples of the form 
    (eigenvalue,algebraic multiplicity,[eigenvectors])
    
    Note that since eigenvects also includes the eigenvalues, 
    you should use it instead of eigenvals if you also want the 
    eigenvectors. However, as computing the eigenvectors 
    may often be costly, eigenvals should be preferred if you 
    only wish to find the eigenvalues.

    If all you want is the characteristic polynomial, use charpoly. 
    This is more efficient than eigenvals, because sometimes 
    symbolic roots can be expensive to calculate.

    To diagonalize a matrix:
    P,D = v.diagonalize()
    where
    P is the matrix to v = P*D*P**-1
    and D is the diagonalized matrix
    '''

def creates_matrix(the_list, rows, cols):
    '''
    I use this function to create a matrix
    from a list of variables.
    The variable list should has the same
    number of rows*cols so that
    I can reshape it into a matrix dim(rows,cols)
    '''
    #mat = zeros(rows,cols)
    
    '''
    if rows*cols == len(the_list):
        #for variable in the_list:
        for row in range(rows):
            for col in range(cols):
                #print(col+row*cols)
                mat[row,col] = the_list[col + row*cols]
    return mat
    '''

    '''
    A more concise solution is to 
    use the Matrix class in sympy
    '''
    return Matrix(rows,cols,the_list)
 

def mat_identity(dim):
    return eye(dim)

def mat_zeros(dim):
    return zeros(dim)

def mat_ones(dim):
    return ones(dim)

def mat_diagonal(number_list):
    '''
    This function creates a square matrix.
    number_list argument is a list.
    To strip down a tuples
    or a list we use *

    return diag(*number_list)

    Matrix classes can also take in lambda function
    
    return Matrix(3,3, lambda i,j: i+1 if i == j else 0)

    or

    return Matrix(3,3, lambda i,j: number_list[i] if i == j else 0)
    '''
    return Matrix(3,3, lambda i,j: number_list[i] if i == j else 0)

def mat_transpose(the_matrix):
    '''
    This function transpose the
    matrix
    
    '''
    return the_matrix.T

def mat_determinant(the_matrix):
    return the_matrix.det()

def mat_row_echelon(the_matrix):
    '''
    The result is a reduced achelon formed matrix
    (matrix,list_of_pivot_cols_indices)

    '''
    return the_matrix.rref()

def mat_nullspace(the_matrix):
    '''
    The result is a list of column vectors that
    span the nullspace of the matrix
    '''
    return the_matrix.nullspace()

def mat_eigenvalues(the_matrix):
    '''
    return a dictionary of {values:multiplicity}
    '''
    return the_matrix.eigenvals()

def mat_eigenvectors(the_matrix):
    '''
    return tuples of the form
    (eigen_values,algebraic_multiplicity, eigenvectors)
    '''
    return the_matrix.eigenvects()

def mat_diagonalize(the_matrix):
    return the_matrix.diagonalize()

def mat_inverse(the_matrix,the_method=None):
    '''
    By default the inverse matrix
    is found using Gaussian elimination
    method (for dense matrix)
    We can specify LU method as well
    '''

    if the_method == None:
        return the_matrix.inv()
    elif the_method.upper() == 'LU':
        return the_matrix.inv(method = the_method.upper())
    else:
        print("The method {}, is unknown".format(the_method))
