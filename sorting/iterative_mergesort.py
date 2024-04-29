"""
Python program implementing an iterative version of the Mergesort

# GENERAL LOGIC:

A list of ONE item is already sorted

Therefore using the example of a list of TWO items 
[3, 1]
 0  1

sublist[0] is already sorted
sublist[1] is already sorted

To merge using power_of2 = TWO
low = 0
high = low + power_of2 - 1  = 1
median = (low + high) // 2 = 0

Beginning with [low = 0] and [median + 1 = 1]

If sublist[0] < sublist[1]
	No!
	Therefore merged[0] = 1
	   		  merged[1] = 3
Hence
merged = [1, 3]


If the list were FOUR ITEMS [3, 1, 2, 6]

Starting with power_of2 = TWO
low = 0
high = low + power_of2 - 1  = 1
median = (low + high) // 2 = 0

So using the above logic:
Beginning with [low = 0] and [median + 1 = 1]

	merged [0] to [1] would be [1, 3]


Then for the second portion

Add 2 to low i.e. low += power_of2 therefore low = 2
high = low + power_of2 - 1  = 3
median = (low + high) // 2 = 2

So using the above logic:
Beginning with [low = 2] and [median + 1 = 3]
	merged [2] to [3] would be [2, 6]

Hence
merged = [1, 3, 2, 6]
Note: both portions are individually sorted


Then double the power_of2 i.e. 2 * 2 = 4
which is <= size of the array 

Therefore
Starting with power_of2 = FOUR

merged = [1, 3, 2, 6]
          0  1  2  3

low = 0
high = low + power_of2 - 1  = 3
median = (low + high) // 2 = 1

Beginning with [low = 0] and [median + 1 = 2]

[1, 3] is merged with [2, 6]
RESULT: merged = [1, 2, 3, 6]


THE LOGIC OF THE FUNCTION merge()

The logic of merge() is as follows:
	left is pointing  to the range array[low .. median - 1]
	right is pointing to the range array[median + 1 .. high]

merged = []
Whilst BOTH left and right are within the range of low .. high:
	if array[left] < array[right]:
		append array[left] to merged
		increment left
	else:
		append array[right] to merged
		increment right

Any remaining items in array[left ... median], append to merged
Any remaining items in array[right ... high],  append to merged



THE LOGIC OF THE FUNCTION mergesort_iterative()

Starting with 2

Since a single item is already sorted
Go through the array in steps of TWO, and merge each sublist of TWO items

Then double the power of 2 i.e. 2*2 = 4
Repeat the merging, this time, each sublist will be FOUR items

Then double the power of 2 i.e. 4*2 = 8
Repeat the merging, this time, each sublist will be EIGHT items
etc.

Repeat this process until the powerof2 is > the size of the array


Therefore if the array was originally an array of e.g. 16 items
The power_of2 would eventually double to = 32
Divide power_of2 by 2 ==> power_of2 //= 2 ==> 32 / 2 = 16
Is 16 less than the size of the array i.e. 16? 
	NO! The Array is now sorted.

However for an array with an ODD number of items e.g. 13
The power_of2 would eventually double to = 16
Divide power_of2 by 2 ==> power_of2 //= 2 ==> 16 / 2 = 8
Is 8 less than the size of the array i.e. 13? 
	YES! 
	Therefore, ONE more merge is needed to finish the sort i.e.
	Merge 0..7 with 8..12
	Hence
	merge(array, 0, power_of2 - 1, arraysize - 1)
	The Array is now sorted.


For any array which size is NOT a Power of 2 e.g. 34
The power_of2 would eventually double to = 64
Divide power_of2 by 2 ==> power_of2 //= 2 ==> 64 / 2 = 32
Is 32 less than the size of the array i.e. 34? 
	YES! 
	Therefore, ONE more merge is needed to finish the sort i.e.
	Merge 0..31 with 32..34
	Hence
	merge(array, 0, power_of2 - 1, arraysize - 1)
	The Array is now sorted.

"""

# Merge two sorted sublists from a single array 
# using low, median and high
def merge(array, low, median, high):
	left = low
	right = median + 1
	merged = []
	while left <= median and right <= high:
		if array[left] < array[right]:
			# Take from the left portion
			merged.append(array[left])
			left += 1
		else:
			# Take from the right portion
			merged.append(array[right])
			right += 1

	# Append any remaining elements from the left portion
	while left <= median:
		merged.append(array[left])
		left += 1
	# Append any remaining elements from the right portion
	while right <= high:
		merged.append(array[right])
		right += 1

	# Replace with sorted sublist
	high = low + len(merged)
	array[low : right] = merged


def mergesort_iterative(array):
	arraysize = len(array)
	# Each pass will be a power of 2 i.e. 2, 4, 8, 16, ...
	power_of2 = 2

	while power_of2 <= arraysize:
		
		# Calculate the low and high using the power of 2
		# Is the range within the size of the array?
		
		low = 0
		while True:
			high = low + power_of2 - 1
			if high >= arraysize:
				break
			median = (low + high) // 2
			merge(array, low, median, high)
			# Move on to the next sublist
			low += power_of2
		power_of2 *= 2
	
	# In the case of when the length of the array is NOT
	# a multiple of a 'power of 2' there will be a remainder sublist
	# Merge that remainder 
	power_of2 //= 2
	if power_of2 < arraysize:
		merge(array, 0, power_of2 - 1, arraysize - 1)

array = [10, 7, 8, 0, -2, 9, -8, 1, 5] # 9 elements
print("Given array is")
print(array)
print("\n")
print("Sorted array is")
mergesort_iterative(array)
print(array)
print("\n")

# Power of 2 - 16 elements
array = [10, 7, 8, 4, 0, -2, 11, 100, 9, 
         -8, 1, 5, -1, 2.6, -0.89, 3.14]
print("Given array is")
print(array)
print("\n")
print("Sorted array is")
mergesort_iterative(array)
print(array)

"""
Output:

Given array is
[10, 7, 8, 0, -2, 9, -8, 1, 5]


Sorted array is
[-8, -2, 0, 1, 5, 7, 8, 9, 10]


Given array is
[10, 7, 8, 4, 0, -2, 11, 100, 9, -8, 1, 5, -1, 2.6, -0.89, 3.14]


Sorted array is
[-8, -2, -1, -0.89, 0, 1, 2.6, 3.14, 4, 5, 7, 8, 9, 10, 11, 100]
"""