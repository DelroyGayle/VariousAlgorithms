

def maximum_product3(numbers):
    """
    Find the maximum product of two numbers in an unsorted list
    The list can contain both negative and positive integers
    Always bear in mind that the product of two negative numbers is positive!
    Therefore regarding the list, such a product could be larger than
    the product of two positive numbers

    Approach 3 - Linear Time Solution
    That is, iterate the list once
    Keep running values of the largest and smallest two numbers

    Output:
    None
    35
    32
    200
    """

    import math

    the_length = len(numbers)
    if the_length < 2:
        print("Minimum two numbers needed to calculate Maximum Product")
        return None

    # largest1, largest2 - largest two numbers found presumably positive
    # smallest1, smallest2 - smallest two numbers found presumably negative
    largest1, smallest1 = numbers[0], numbers[0]
    largest2 = -math.inf
    smallest2 = math.inf

    for i in range(1, the_length):
        # Determine the largest two numbers
        if numbers[i] > largest1:
            largest2 = largest1
            largest1 = numbers[i]
        elif numbers[i] > largest2:
            largest2 = numbers[i]

        # Determine smallest number
        if numbers[i] < smallest1:
            smallest2 = smallest1
            smallest1 = numbers[i]
        elif numbers[i] < smallest2:
            smallest2 = numbers[i]

    max_product = largest1 * largest2
    min_product = smallest1 * smallest2
    return max_product if max_product > min_product else min_product


print(maximum_product3([]))
print(maximum_product3([5, 3, 2, 5, 7, 0, 1]))
print(maximum_product3([-2, -1, -3, 4, 8, 0]))
print(maximum_product3([-20, -10, 3, 9, 8]))
