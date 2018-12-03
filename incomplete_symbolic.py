'''
This module explains how to use
symbolic variables and the symbolic 
modules
'''

from sympy import symbols, expand, init_printing, Eq

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
    
    Returns bool value
    '''
    return a.equals(b)
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

def latex_it(expression):
    '''
    '''

def solves(expression, root):
    '''
    '''
"""
