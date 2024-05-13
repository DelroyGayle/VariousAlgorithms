
"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are
in the range [1, n] and each integer appears once or twice,
return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time
and uses only constant extra space.


Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]


Example 3:
Input: nums = [1]
Output: []


Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n

Each element in nums appears once or twice.

"""


def find_all_duplicates_1(array):
    """
    Method 1
    By making use of the fact that all integers in the array are
    in the range [1, n] and each integer appears once or twice:
    1) iterate through the array
    2) take the value of an element and ensure it is positive
    3) Then using it as an 'index' i.e. array[index],
       mark each 'visited' element 'array[index]' by making it negative!
       (NOTE: Because Indexing in Python starts at 0,
        subtract 1 from 'index' therefore 'array[index - 1]')
    4) If 'array[index - 1]' is found to be already negative
       i.e. already 'marked' as visited, then the value 'index' is a duplicate,
       otherwise make 'array[index - 1]' negative.

    """

    results = []
    the_length = len(array)

    for i in range(the_length):
        # Ensure that the index is positive
        # Subtract 1 to cater for zero-indexing
        index = abs(array[i])
        index_minus1 = index - 1
        if array[index_minus1] < 0:
            # Already negative hence it is a duplicate
            results.append(index)
        else:
            # Mark as visited by making the value negative
            array[index_minus1] = -array[index_minus1]

    return results


def find_all_duplicates_2(array):
    """
    Method 2

    1) Iterate through the array - 'n' is the length of the array
    2) Decrement by 1 to ensure within the range 0 <= i <= n - 1
       i.e. (array[i] - 1)
    3) Calculate index = (array[i] - 1) % n
    4) Then add n to array[index]
    5) When the iteration is done, iterate through the array again
    6) Divide each element by n
       If an element has a quotient >= 2,
       then the index of that element represents a duplicate
    7) However Increment by 1 to ensure within the range 1 <= i <= n
       i.e. i + 1

    Therefore, any array[i] / n would be >= 2
    only if a value 'i' has appeared more than once.

    """

    results = []
    the_length = len(array)
    if the_length == 1:
        return []

    for i in range(the_length):
        # Decrement by 1 to ensure within the range 0 <= i <= n - 1
        # Then calculate the modulus
        index = (array[i] - 1) % the_length

        # Calculate the sum
        array[index] += the_length

    # Fetch indices of elements where the quotient is >= 2
    # Increment by 1 to ensure within range 1 <= i <= n

    for i in range(the_length):
        if (array[i] // the_length) >= 2:
            results.append(i + 1)

    return results


print(find_all_duplicates_1([1]))  # []
print(find_all_duplicates_1([1, 1, 2]))  # [1]
print(find_all_duplicates_1([2, 1, 2]))  # [2]
print(find_all_duplicates_1([2, 1, 1]))  # [1]
print(find_all_duplicates_1([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
print(find_all_duplicates_1([1, 3, 2, 1]))  # [1]
print()
print(find_all_duplicates_2([1]))  # []
print(find_all_duplicates_2([1, 1, 2]))  # [1]
print(find_all_duplicates_2([2, 1, 2]))  # [2]
print(find_all_duplicates_2([2, 1, 1]))  # [1]
print(find_all_duplicates_2([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
print(find_all_duplicates_2([1, 3, 2, 1]))  # [1]
