# Filter

### I have an array and I want to return a new array with certain elements of the old array

### The filter function is called with a lambda function or a named function, defining a condition 

#### that condition will define which element of the original array to place into the new array

### filter does a type check on the arguments (list, function) and returns a canned printout if False

## example

    new_array = filter([1,2,3,4,5],lambda x: x > 2)

#### new_array is [3,4,5]

### here is an example of filter using a named function

    def is_greater_than_2(item):

        if (item > 2):

            return True

        else:

            return False

    new_array = filter([1,2,3,4,5],is_greater_than_2)

### new_array is [3,4,5] when using the named function, also

