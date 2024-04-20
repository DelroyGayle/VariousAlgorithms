# Python program implementing an iterative version of the Quicksort

"""
This function takes the last element as the pivot.
It places the pivot element at its correct position
in the sorted array.
That is, it places all smaller (i.e. smaller than pivot) to
the left of the pivot and all greater elements
to the right of the pivot.
"""


def partition(array, low, high):
    i = (low - 1)           # index of smaller element
    pivot = array[high]     # pivot

    for j in range(low, high):

        # If the current element is smaller
        # than or equal to the pivot
        # then increment the index of the smaller element
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swop the pivot element into the correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    # Resultant pivot position
    return i + 1

# Iterative Quick Sort function
# array[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index


def quicksort_iterative(array, low, high):

    # Create an auxiliary stack
	arraysize = high - low + 1
	stack = [0] * arraysize

	# initialise the stack pointer
	stack_pointer = -1

	# push the initial values of low and high onto the stack
	stack_pointer += 1
	stack[stack_pointer] = low
	stack_pointer += 1
	stack[stack_pointer] = high

	# Keep processing values from the stack while it is not empty
	while stack_pointer >= 0:

		# Pop the high and low values
		high = stack[stack_pointer]
		stack_pointer -= 1
		low = stack[stack_pointer] 
		stack_pointer -= 1

		# Set the pivot element at its correct position in 
		# the sorted array 
		pivot_index = partition(array, low, high) 

		# If there are elements on the left side of the pivot, 
		# then push the left side range on to the stack 
		if pivot_index-1 > low: 
			stack_pointer += 1
			stack[stack_pointer] = low 
			stack_pointer += 1
			stack[stack_pointer] = pivot_index - 1

		# If there are elements on the right side of the pivot, 
		# then push the right side range on to the stack 
		if pivot_index + 1 < high: 
			stack_pointer += 1
			stack[stack_pointer] = pivot_index + 1
			stack_pointer += 1
			stack[stack_pointer] = high 

array = [2, 8, -7, 1, 0, 3, 5, 6, -4] 
n = len(array) 
quicksort_iterative(array, 0, n-1) 
print("Sorted array is:") 
print(array) 

"""
Output:

Sorted array is:
[-7, -4, 0, 1, 2, 3, 5, 6, 8]
"""
