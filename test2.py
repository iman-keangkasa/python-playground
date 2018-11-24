"""
This modules has functions for Chp4 in 
Guttag's Python (1013)

Scopes of a modules or a functions is also know sa
Namespace
"""
import incomplete_tables as tables

def isIn(a,b):
    if a in b:
        print("Yes")
        return True
    else:
        return False
        print("Nay")

def robotName(a='robot',b='roboto',reverse=False):
    if reverse:
        print('{1}, {0}'.format(a.title(), b.title() ))
    else:
        print('{0} {1}'.format(a.title(), b.title() ))

def findRoot(x, power, epsilon, method=0):
    """
    Finding a more generalized exhaustive enumeration method using
    bisection algorithm

    Usage:
        findRoot(x, power, epsilon, method)
        x the number of the root
        power is the power of the x
        epsilon is the halting requirement ~ approaching 0
        if method == 1, do bisection
        if method == 0, do newton
        if method == default, do newton
    """
    if x < 0:
        x_abs = abs(x)
        sign = -1
        
    else:
        x_abs = x
        sign = 1

    trials = 0

    if method == 1:
        low = 0
        high = x_abs
        mid = (high + low)/2 #mid point is the approximation of the root
        #headers = ['Trial', 'Low', 'High', 'Root', 'Epsilon' ]
        #width = 10
        #incomplete_tables.online_numeric_table(headers, width=10, header=True)

        width = 13 
        decimal = 2

        ###START TABLING ###
        header_content=['Trial','Low','High','Root','Epsilon']
        tables.table_header(header_content, width)  
        while abs(mid**power - x_abs) >= epsilon:
            trials += 1
            if mid**power < x_abs:
                low = mid
            else:
                high = mid
            mid = (high+low)/2.0
            error = abs(mid**power - x_abs)
#            print( "|{0:^10}|{1:^10.3f}|{2:^10.3f}|{3:^10.3f}|{4:^10.3f}|".format(
#                   trials, sign*low, sign*high, sign*mid, error) ) 
            numeric_list= [trials, sign*low, sign*high, sign*mid, error]
            tables.table_content(numeric_list, width, decimal)
        tables.vertical_borders(len(numeric_list), width)
        ### END TABLING ###
    else:
        guess = x_abs/2.0
        width = 10
        decimal = 2
 
        header_list=['Trials','Root', 'Epsilon']
        tables.table_header(header_list, width)
        while abs(guess**power - x_abs) >= epsilon:
            trials += 1
            guess = guess - ( (guess**power - x_abs) / ((power)*guess**(power-1)) )
            error = abs(guess**power - x_abs)
#           var_list = [trials, guess*sign, error]
#           incomplete_tables.online_numeric_table(var_list, width = 10, decimal = 3)
            tables.table_content([trials, guess*sign, error], width, decimal)
        tables.vertical_borders(len(header_list),width)

