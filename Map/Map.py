# map


def map(arr, f):

    
    if(type(arr) is list and hasattr(f,'__call__')):
        
        return [f(x) for x in arr]
    else:
        return "Check correct Type of arguments"

'''
# testing
print(mymap([1,2,3,4,5],lambda x: x * 2))
'''
