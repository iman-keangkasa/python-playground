'''
This module attempts to emulate the bash
script I fond of. I will use subprocess module
and the os module to accomplish this

so far I have done:
    [/] ls 
    [x] cd
    [x] rm
    [x] cp
    [x] mv
    [x] vim?
'''


import subprocess, os 

def ls(the_path=None):
    if the_path == '~':
        subprocess.call([ 'ls', os.environ['HOME'] ])
    elif the_path == None:
        subprocess.call('ls')
    else: 
        if '~' in the_path:
            the_path = the_path.replace('~', os.environ['HOME'])
        subprocess.call(['ls',the_path])

    
