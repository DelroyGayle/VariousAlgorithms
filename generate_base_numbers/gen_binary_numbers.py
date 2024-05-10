def generate_binary_numbers(n):
    """
    Generate 'n' binary numbers using a 'queue'
    That is, generate the first 'n' binary numbers
    The algorithm must take in an integer 'n' as input and return
    a list of the first 'n' binary numbers.
    """

    result = []
    if n <= 0:
        return result

    queue = ['1']
    for i in range(0, n):
        current = queue.pop(0)
        result.append(current)
        for j in range(2):
            queue.append(current + str(j))

    return result


print(generate_binary_numbers(0))
print(generate_binary_numbers(1))
print(generate_binary_numbers(2))
print(generate_binary_numbers(6))
print(generate_binary_numbers(16))
