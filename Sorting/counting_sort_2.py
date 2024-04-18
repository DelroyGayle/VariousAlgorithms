# METHOD 2
# Calculate the sorted_array from RIGHT TO LEFT
def counting_sort_2(input_array):
  largest_number = max(input_array)  # EG 3
  the_size = largest_number + 1
  indices_array = []
  # store the count of each unique element of the input array
  # at their respective indices
  for i in range(the_size):
    indices_array.append(input_array.count(i))
  # EG indices_array ==> [1, 3, 0, 2]

  # ADD EACH NUMBER CUMULATIVELY
  # Calculating prefix sum at every index of count_array
  for i in range(1, the_size):
    indices_array[i] += indices_array[i - 1]

  # EG indices_array ==> [1, 4, 4, 6]

  # Set up the Result Array
  sorted_array = [0] * len(input_array)

  # Place each item from the original array into its sorted position
  # That is, Starting from the right
  # Traverse array input_array[] from end
  # the_index = indices_array[ input_array[i] ] - 1
  # update sorted_array[ the_index ] = input_array[i]

  for i in range(len(array) - 1, -1, -1):
    the_index = indices_array[input_array[i]] - 1
    # Increment it for the next possible iteration
    indices_array[array[i]] = the_index
    sorted_array[the_index] = input_array[i]

  return sorted_array


# Driver code
array = [1, 0, 3, 1, 3, 1]
sorted_array = counting_sort_2(array)
print(sorted_array)
# RESULT
# [0, 1, 1, 1, 3, 3]


array = [8, 3, 5, 1, 3, 8, 6, 4, 3]
sorted_array = counting_sort_2(array)
print(sorted_array)
# RESULT
# [1, 3, 3, 3, 4, 5, 6, 8, 8]

array = [2, 5, 3, 0, 2, 3, 0, 3]
sorted_array = counting_sort_2(array)
print(sorted_array)
# RESULT
# [0, 0, 2, 2, 3, 3, 3, 5]
