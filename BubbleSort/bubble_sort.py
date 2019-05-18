#bubble sort

arr = [1,4,2,8,4,7,20,3]


sorted_array = []

while (arr):

    

    for i in range(len(arr)-1,0,-1):

        if (arr[i] < arr[i-1]):

            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            
    sorted_array.append(arr.pop(0))

 
print sorted_array
