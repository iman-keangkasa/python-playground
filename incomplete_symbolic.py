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

from sympy import symbols, expand, factor, init_printing, Eq, simplify, sympify, lambdify, collect, cancel, apart, trigsimp, expand_trig

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
    sympt.factor(expression)
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
    sympy.cancel simplify a rational function into
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
