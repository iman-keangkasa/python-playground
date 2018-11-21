'''
This modules/programs make ASCII table
'''
# Parameters needed, decimal points, significant figures?
# Rules: Makes content from the borders at least 1 characters away

variables = 9
topBot ='+{0:-^{1}}'.format("",padding) # +-----
topBotEnd ='+'                          # +
middle='|{0:^{1}}'.format(variables,padding)   # |    
middleEnd ='|'                          # |


def end_tabling(cols):
    print(cols*topBot + topBotEnd)

def tabling():
    decimal_point = 2
    padding = 5 #padding gives the number of size of each box
    cols = 9
    rows = 3
    
    for row in range(rows):
        print(cols*topBot + topBotEnd)
        print(cols*middle + middleEnd)
   
    end_tabling(cols)
   
