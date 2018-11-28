"""
This module is used to handle file:
-creation
-writing
-reading
-appending
"""

def write(data):
    '''
    To write a file
    use nameHandle=open('data', 'w')
    The same file name will have its content erased
    '''
    nameHandle = open(data, 'w')
    nameHandle.write('Micheal\t12\n')
    nameHandle.write('Greg\t13\n')
    nameHandle.close()
    nameHandle = open(data, 'r')
    for line in nameHandle:
        print(line[:-1])
    nameHandle.close()

def read(data):
    '''
    To read a file
    '''
    nameHandle = open(data, 'r')
    for line in nameHandle:
        print(nameHandle.readline())
    nameHandle.close()
def copy(a,b):
    '''
    Copy a file to a newfile
    copy(a,b)
    a is a str of file to copy
    b is a str of file to create and hv content of a
    '''

def add():
    '''
    '''
def auto_rename():
    ''''''

