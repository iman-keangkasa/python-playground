'''
List all variables/modules currently in my current session
'''
def listall(a):
#    v = locals()
    for key, value in a.items():
        print('{0} --- {1:^10}'.format(key,value))
    print("Execution Done!")
