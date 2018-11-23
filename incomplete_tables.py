'''
This modules/programs make ASCII table
'''
# Parameters needed, decimal points, significant figures?
# Rules: Makes content from the borders at least 1 characters away

cell_width = 10

variables = 9
topBot ='+{0:-^{1}}'.format("",padding) # +-----
topBotEnd ='+'                          # +
middle='|{0:^{1}}'.format(variables,padding)   # |    
middleEnd ='|'                          # |

def the_cell(element, width=20, decimal=0, numerical=False):
    if numerical:
        None
    else:
        return middle='|{0:^{1}}'.format(variables, width)

def end_tabling(cols):
    print(cols*topBot + topBotEnd)

def tabling():
    decimal_point = 2
    padding = cell_width #padding gives the number of size of each box
    cols = 9
    rows = 3
    
    for row in range(rows):
        for col in range(cols)
        print(cols*topBot + topBotEnd)
        print(cols*middle + middleEnd)
   
    end_tabling(cols)
'''
def table_header(header_list):
    for col in range( len(header_list) ):
        cell = the_cell(header_list[col], width = 10)
        print(cell, end='')
    print(middleEnd)
    print(topBot, topBotEnd)

'''
