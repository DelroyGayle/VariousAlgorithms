"""
Radix Sort - least significant digit (LSD) approach
"""

TEN = 10

def radix_sort(array):
    arraysize = len(array)
    divisor = 1
    while True:
        bucket = [[] for _ in range(TEN)]
        nonzero = False
        for i in range(arraysize):
            # remainder = (array[i] // divisor) % TEN
            quotient = array[i] // divisor
            if quotient > 0:
                nonzero = True
            remainder = quotient % TEN
            bucket[remainder].append(array[i])

        if not nonzero:
            # All zero quotients means the array is sorted!
            return array

        array = []
        for i in range(TEN):
            array.extend(bucket[i])

        divisor *= TEN # 1, 10, 100, 1000, etc


array = [237, 146, 259, 348, 152, 163, 235, 48, 36, 62, 891, 1000,
         2111, 1, 0] 
n = len(array) 
sorted = radix_sort(array) 
print("Sorted array is:") 
print(sorted) 

"""
Output:

Sorted array is:
[0, 1, 36, 48, 62, 146, 152, 163, 235, 237, 259, 348, 891, 1000, 2111]
"""