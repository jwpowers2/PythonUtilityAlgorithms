# reduce

def myreduce(iterable, func, start=None):
    it = iter(iterable)
    if start is None:
        try:
            start = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = start
    for x in iterable:
        accum_value = func(accum_value, x)
    return accum_value

total = myreduce([1,2,3,4,5],lambda x,y: x + y)
print(total)
