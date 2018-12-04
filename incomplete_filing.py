"""
This module is used to handle file:
-creation
-writing
-reading
-appending

data is the location (and name) of the text file
"""

def write(data):
    '''
    To write a file
    use nameHandle=open('data', 'w')
    The same file name will have its content erased
    '''
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
def replace_pattern(data,pattern1,pattern2):
    '''
    buggy the list of lines becomes just one line

    data is the location/name of the file
    pattern2 will replace pattern1
    
    
    '''
    fh = open(data, 'r')
    lines = fh.readlines()
    fh.close()
    for index, line in enumerate(lines):
        lines[index] = line.replace(pattern1, pattern2)
    return lines
    #fh = open(data, 'w')
    #fh.writelines(lines)
    fh.close()
