'''
This modules/programs make ASCII table
'''
# TO-DO LIST
# make tabling for dictionary
# make tabling for 2D list / 2D tuples
# make tabling for numpy arrays

def topBot(padding):
    return '+{0:-^{1}}'.format("",padding) # +-----

def row_contents(variables, width=10, decimal=3, numeric=False):
    if numeric:
        for variable in variables:
            if type(variable).__name__ == 'int':
                print('|{0:^{1}}'.format(variable,width), end='')
            if type(variable).__name__ == 'float':
                print('|{0:^{1}.{2}f}'.format(variable, width, decimal), end='')
        print('|')
    else:
        for variable in variables:
            print('|{0:^{1}}'.format(variable,width), end='')
        print('|')

def vertical_borders(cols,width):
    print(cols*topBot(width), end='')
    print('+')

def table_header(the_list, table_width=10):
    cols = len(the_list)
    vertical_borders(cols, table_width)    
    row_contents(the_list, table_width)  
    vertical_borders(cols,table_width)

def table_content(the_list, table_width=10, table_decimal=3):
    cols = len(the_list)   
    row_contents(the_list, table_width, table_decimal, True)
    

