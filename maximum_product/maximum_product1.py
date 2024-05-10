

def maximum_product1(numbers):
    """
    Find the maximum product of two numbers in an unsorted list
    The list can contain both negative and positive integers
    Always bear in mind that the product of two negative numbers is positive!
    Therefore regarding the list, such a product could be larger than 
    the product of two positive numbers

    Approach 1 - Iterate through the list - Complexity O(n^2)

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

    maximum = -math.inf
    for i in range(the_length):
        for j in range(i + 1, the_length):
            product = numbers[i] * numbers[j]
            if product > maximum:
                maximum = product

    return maximum


print(maximum_product1([]))
print(maximum_product1([5, 3, 2, 5, 7, 0, 1]))
print(maximum_product1([-2, -1, -3, 4, 8, 0]))
print(maximum_product1([-20, -10, 3, 9, 8]))
