'''
My files to remember 
what are escape characters I need
with my strings
'''
backslash = '\\'
single_quotes = "\\\'"
double_quotes = '\\"'
bell_ringing = '\\a'
removes_previous_char = "\_any_char"
formfeed = '___\\f___'
formfeed_result = '___\f___'
linefeed = '___\n___'
linefeed = '___\\n___'
unicode_utf ='\\uxxxx'
unicode_utf16 ='\\UXXXXXXXX'

def arrowDown(a):
    arrow0 = '\u2510'
    arrow1 = '\u2502'
    arrow2 = '\u2514'
    arrowHead ='\u21E2'
    padding = a+1
    print('{0}\n{1:>{2}}\n{3:>{2}}{4}'.format(arrow0,arrow1,padding,arrow2,arrowHead), end='')

def printing_hex():
    '''
    this function shows 
    how to print hexadecimal number
    '''
    print("To print a hex number, use format\n")
    this="print({0:#5x}.format(177)"
    a=len(this)
    print(this, end='')
    arrowDown(a)
    print('{0:#5x}'.format(177))


