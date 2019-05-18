# selection sort
# malfunctions with duplicates in array, need to fix

class SelectionSort(object):


    def sort_min(self, arr):


        for i in range(0,len(arr)):

            minimum = arr[i]
            min_index = i

            for x in range(i,len(arr)):

                if arr[x] < arr[i]:

                    minimum = arr[x]
                    min_index = x

                else:
 
                    minimum = arr[i]
                    min_index = i

            temp = arr[i]
            arr[i] = minimum
            arr[min_index] = temp
        
        return arr

    def sort_max(self, arr):

        for i in range(0,len(arr)):

            maximum = arr[i]
            max_index = i

            for x in range(i,len(arr)):

                if arr[x] > arr[i]:

                    maximum = arr[x]
                    max_index = x

            temp = arr[i]
            arr[i] = maximum
            arr[max_index] = temp
        
        return arr

