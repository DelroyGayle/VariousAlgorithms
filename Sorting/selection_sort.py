# Python program for the implementation of 
# Selection Sort
array = [64, 25, 12, -3, -9, 22, 11]

# Traverse through all array elements
for i in range(len(array)-1):
    
    # Find the minimum element in remaining 
    # unsorted array
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            
    # Swap the found minimum element with 
    # the first element        
    array[i], array[min_index] = array[min_index], array[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(array)):
    print(array[i],end=" ") 


"""
Output:

Sorted array
-9 -3 11 12 22 25 64 
"""