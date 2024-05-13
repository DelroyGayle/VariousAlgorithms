"""
https://leetcode.com/problems/single-number/description/

136. Single Number

Given a non-empty array of integers nums,
every element appears twice except for one.

Find that single one.

You must implement a solution with a linear runtime complexity
and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104

Each element in the array appears twice except for one element
which appears only once.
"""


def solve_with_sort(array):
    """
    1) Sort the array.
    2) Traverse the array and check if one of the adjacent elements
       is equal to the current element.
    3) If True, continue to the next element
    If False, return the current element as the solution
    """

    array.sort()
    the_length = len(array)
    if the_length == 1:
        return array[0]

    for i in range(0, the_length - 1, 2):

        if array[i] != array[i + 1]:
            return array[i]

    return array[the_length-1]


def solve_with_xor(array):
    """
    In Binary Logic the following rule applies to the XOR operator:

    A B     A^B
    0 0      0
    0 1      1
    1 0      1
    1 1      0

    That is, when the bits are identical the result is 0
    Therefore,
    1) A^A = 0
    2) A^B^A=B
    3) (A^A^B) = (B^A^A) = (A^B^A) = B
    Therefore, the order does not matter.
    4) So for an even number of duplicates the result will cancel out to ZERO
    However for an even number of duplicates and one non-duplicate number;
    that is, an odd number of items;
    the result will be the non-duplicate number

    Use this fact to determine this single number
    """

    result = 0
    for number in array:
        result ^= number

    return result


print(solve_with_sort([2, 2, 1]))  # 1
print(solve_with_sort([4, 1, 2, 1, 2]))  # 4
print(solve_with_sort([1]))  # 1
print(solve_with_sort([2,  2,  3,  4,  4]))  # 3
print(solve_with_sort([2,  2,  -3,  -4,  -4]))  # -3

print()

print(solve_with_xor([2, 2, 1]))  # 1
print(solve_with_xor([4, 1, 2, 1, 2]))  # 4
print(solve_with_xor([1]))  # 1
print(solve_with_xor([2, 2, 3, 4, 4]))  # 3
print(solve_with_sort([2,  2,  -3,  -4,  -4]))  # -3
