'''
This module explains how to use
symbolic variables and the symbolic 
modules

TODO:
    for partial_decomp find a way to get the
    zeros and the roots for control application
    
    for partial_decomp find a way to isolate 
    each terms from the result

    3/12/2018 stops at Powers and Special Functions
'''

from sympy import symbols, expand, factor, init_printing, Eq, simplify, sympify, lambdify, collect, cancel, apart, trigsimp, expand_trig, powsimp, expand_power_exp, expand_power_base, powdenest, expand_log, logcombine, factorial, binomial, combsimp, diff, Derivative

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
    respect_to should be a list of how the derivative
    should be evaluated according to the
    variable and order of the list
    
    BUGGY! INCOMPLETE COME BACK LATER

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
        terminate = len(n)
        args = ''
        for index, element in enumerate(respect_to):
            if index < terminate-1:
                args = args + str(element) + ',' + str(n[index]) + ','
            else:
                args = args + str(element) + ',' + str(n[index])
#        print(args)
        return expression.diff(*eval(n))


def integrates(expression):
    '''
    The integrates can be invoke as a function 
    or a method
    sympy.integrates(expression, (reference,lower_limit,upper_limit))
    or
    sympy.integrates(expression, reference)

    The Integral function is used to integrate the indef
    sympy.Integral( expression, (respect, lower_limit, upper_limit) )
    or
    sympy.Integral(expression, respect)

    Integral function will only evaluate the integration by invoking the
    doit() method.
    '''

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
#SOLVE


"""
def integrates(expression):
    '''
    '''

def differentiates(expression):
    '''
    '''

def limits(expression,limit):
    '''
    '''
def solve_diff(expression, respect):
    '''
    '''
def eigens(expression):
    '''
    '''

def solves(expression, root):
    '''
    '''
"""
