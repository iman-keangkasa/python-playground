"""
Testing different concepts in Python programming 
and computations
"""

def multiple_return():
    """Testing multiple returns.
    syntax: v,w = test.multiple_return()
    v = 5
    w = 6"""

    a = 5
    b = 6
    return a, b

def separate_dict(a):
    """The way to separate a dictionary keys
    and values"""
    keys, value = zip(*a.items()) #a.items() returns tuples 
                                  #* unpack the tuples
    return keys, value

def looping():
    x = 4
    for i in range(x):
        for j in range(x):
            print(j) 
            x = 2 #will not change the number of iteration for j since j has been eval 
            #print("x = 2 starts here")

def strings_sum():
    '''
    This functions reads a stream of comma separated strings, s
    convert them into numbers and add them up 
    I use s.split(',')
    '''
    s = '1.23,2.4,3.123'
    total = 0
    s=s.split(',')

    for number in s:
        total = total + float(number)
    
    return s

def strings_sum2():
    '''
    This function uses a different approach where it reads
    the string for comma separated string, s and add them 
    up
    '''
    def summing(string,total):
        total = float(string) + total
        return total
    
    s = '1.23,2.4,3.123,1,0,1,1,1'
    total = float()
    num = ''
    terminate = 0
    for i in s:
        
        terminate = terminate + 1

        if i != ',':
            num = num + i
            if terminate == len(s):
                total = summing(num,total)
                print(total)
            #print(num)
        else:
            total = summing(num,total)
            print(num)
            print(total)
            num = ''

def sqrt(x):
    '''
    I am implementing bisection searching algorithm
    in this function
    '''
    epsilon = 0.01
    low = 0.0
    high = max(1.0,x)
    numGuesses = 0
    ans = (high+low)/2.0

    print('{0:^20}{1:^20}{2:^20}{3:^20}{4:^20}'.format(
        'Trial','Low','High','Ans','Error/Epsilon'))
    
    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0

        print('{0:^20}{1:^20.2f}{2:^20.3f}{3:^20.3f}{4:^20.3f}'.format(
            numGuesses, low, high, ans, abs(ans**2-x) ))

    print("Number of guesses: ",numGuesses)
   
def cube_root(x):
    epsilon = 0.01
    low = 0
    high = abs(x)
    abs_x = abs(x)
    if x < 0:
        negative = True
        sign = -1
    else:
        sign = 1
    ans = (high+low)/2
    trials = 0
    print('{0:^20}{1:^20}{2:^20}{3:^20}'.format('Trial','High','Low','Approximation'))
    while abs(ans**3 - abs_x) >= epsilon:
        trials += 1
        if ans**3 < abs_x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
        print('{0:^20}{1:^20.3f}{2:^20.3f}{3:^20.3f}'.format(
             trials,sign*high, sign*low, sign*ans))

def newton_raphson(x):
    """
    Newton stated that: if you have a guess/approximation
    guess - p(guess)/p'(guess)  is always better
    """
#    if x:
#        print("Please enter a number")
        
#    def square_root(x):
#        """
#        Find square root x such that x**2-guess is within epsilon 0
#        """
    epsilon = 0.01
    
    guess = x/2
    trial = 0
    print('{0:^20}{1:^20}{2:^20}'.format('Trial', 'Guess', 'Error/epsilon'))
    while abs(guess*guess - x) >= epsilon:
        trial += 1
        guess = guess - ((guess**2 -x) / (2*guess))

        print('{0:^20}{1:^20.3f}{2:^20.3f}'.format(trial, guess, guess**2 - x ))

