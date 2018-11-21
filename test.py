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
    s = '1.23,2.4,3.123'
    total = 0
    s=s.split(',')

    for number in s:
        total = total + float(number)
    
    return s

def strings_sum2():
    
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

def finding_sqrt(x):
    '''
    I am implementing bisection searching algorithm
    in this function
    '''
    epsilon = 0.01
    low = 0.0
    high = max(1.0,x)
    numGuesses = 0
    ans = (high+low)/2.0
    
    while abs(ans**2 - x) >= epsilon:
        print('Low: ', low, 'high: ', high, 'ans= ', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0

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
    while abs(ans**3 - abs_x) >= epsilon:
        trials += 1
        print('Trial: ',trials,"High: ", sign*high, "Low: ", sign*low, "Ans: ", sign*ans)
        if ans**3 < abs_x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2

