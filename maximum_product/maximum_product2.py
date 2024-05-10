

def maximum_product2(numbers):
    """
    Find the maximum product of two numbers in an unsorted list
    The list can contain both negative and positive integers
    Always bear in mind that the product of two negative numbers is positive!
    Therefore regarding the list, such a product could be larger than
    the product of two positive numbers

    Approach 2 - Use Sort
    If the list contains negative numbers, then after a sort,
    indices [0] and [1] would contain the smallest negative numbers
    whilst [length-2] and [length-1] would contain the largest positive numbers
    i.e. note that -60 * -100 is greater than 30 * 10

    Output:
    None
    35
    32
    200
    """

    the_length = len(numbers)
    if the_length < 2:
        print("Minimum two numbers needed to calculate Maximum Product")
        return None

    numbers.sort()
    max_product = numbers[the_length - 2] * numbers[the_length - 1]
    min_product = numbers[0] * numbers[1]
    return max_product if max_product > min_product else min_product


print(maximum_product2([]))
print(maximum_product2([5, 3, 2, 5, 7, 0, 1]))
print(maximum_product2([-2, -1, -3, 4, 8, 0]))
print(maximum_product2([-20, -10, 3, 9, 8]))
