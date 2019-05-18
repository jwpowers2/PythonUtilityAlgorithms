# filter 

def myfilter(arr, f):
        
    if(type(arr) is list and hasattr(f,'__call__')):
        
        return [x for x in arr if f(x)]
    else:
        return "Check correct Type of arguments"

'''
#++++++++++ lambda example +++++++++++

print(myfilter([1,2,3,4,5],lambda x: x > 2))
#++++++++++ named function example +++++++++++

def is_greater_than_2(item):

    if (item > 2):

        return True

    else:

        return False

print(myfilter([1,2,3,4], is_greater_than_2))

''' 

