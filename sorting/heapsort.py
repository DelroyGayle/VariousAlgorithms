# Heap Sort in Python

def heapify(array, arraysize, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < arraysize and array[i] < array[l]:
        largest = l

    if r < arraysize and array[largest] < array[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, arraysize, largest)


def heapSort(array):
    arraysize = len(array)

    # Build max heap
    for i in range(arraysize//2, -1, -1):
        heapify(array, arraysize, i)

    for i in range(arraysize-1, 0, -1):
        # Swap
        array[i], array[0] = array[0], array[i]

        # Heapify root element
        heapify(array, i, 0)


array = [1, 12, 9, 5, 6, 10]
heapSort(array)
arraysize = len(array)

print("Sorted array is")
for i in range(arraysize):
    print("%d " % array[i], end='')
print("\n")

array = [10, 7, 8, 4, 0, -2, 11, 100, 9, 
         -8, 1, 5, -1, 26, 89, 13]
heapSort(array)
arraysize = len(array)

print("Sorted array is")
for i in range(arraysize):
    print("%d " % array[i], end='')
print("\n")

"""
Sorted array is
1 5 6 9 10 12 

Sorted array is
-8 -2 -1 0 1 4 5 7 8 9 10 11 13 26 89 100 
"""