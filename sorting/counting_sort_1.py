
# DEMONSTRATE COUNTING SORT


def counting_sort(array):
    largest_number = max(array)  # EG 3
    the_size = largest_number + 1
    # indices_array = [0] * the_size
    indices_array = []
    # COUNTING THE OCCURRENCES OF EACH NUMBER IN THE ARRAY
    for i in range(the_size):
        indices_array.append(array.count(i))
    # EG indices_array ==> [1, 3, 0, 2]
    # ADD EACH NUMBER TO THE RIGHT OF IT CUMULATIVELY
    sum = indices_array[0]
    for i in range(1, the_size):
        sum += indices_array[i]
        indices_array[i] = sum

    # EG indices_array ==> [1, 4, 4, 6]
    # indices_array[0:-1] ==> [1, 4, 4]
    # [0] + indices_array[0:-1] ==> [0, 1, 4, 4]

    # SHIFT THE WHOLE ARRAY TO THE RIGHT BY ONE CELL
    indices_array = [0] + indices_array[0:-1]

    # Set up the Result Array
    sorted_array = [0] * len(array)

    # Place each item from the original array into its sorted position
    for i in range(len(array)):
        the_index = indices_array[array[i]]
        # Increment it for the next possible iteration
        indices_array[array[i]] += 1
        sorted_array[the_index] = array[i]

    return sorted_array


# Driver code
array = [1, 0, 3, 1, 3, 1]
sorted_array = counting_sort(array)
print(sorted_array)
# RESULT
# [0, 1, 1, 1, 3, 3]


array = [8, 3, 5, 1, 3, 8, 6, 4, 3]
sorted_array = counting_sort(array)
print(sorted_array)
# RESULT
# [1, 3, 3, 3, 4, 5, 6, 8, 8]
