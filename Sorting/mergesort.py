# Recursive Python Program for merge sort

def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result


def mergesort(list):
	if len(list) < 2:
		return list

	middle = int(len(list)/2)
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)


array = [10, 7, 8, 0, -2, 9, -8, 1, 5]
print("Given array is")
print(array)
print("\n")
print("Sorted array is")
print(mergesort(array))

"""
Output:

Given array is
[10, 7, 8, 0, -2, 9, -8, 1, 5]


Sorted array is
[-8, -2, 0, 1, 5, 7, 8, 9, 10]
"""