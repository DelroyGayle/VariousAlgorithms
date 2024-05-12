# https://leetcode.com/problems/missing-number/description/

"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.


Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers,
             so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers,
             so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers,
             so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

"""


def solve(array):
    """
    The sum of 0 ... n = n/2 * (n + 1)
    Use this fact to determine the missing number
    """

    n = len(array)
    sum = int(n/2 * (n + 1))

    for i in array:
        sum = sum - i

    return sum


print(solve([3, 0, 1]))  # 2
print(solve([0, 1]))  # 2
print(solve([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
