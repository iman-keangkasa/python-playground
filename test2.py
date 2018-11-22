"""
This modules has functions for Chp4 in 
Guttag's Python (2013)

Scopes of a modules or a functions is also know sa
Namespace
"""
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
