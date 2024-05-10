def generate_binary_numbers(n):
    """
    Generate 'n' binary numbers using the Python 'Queue' data structure
    That is, generate the first 'n' binary numbers
    The algorithm must take in an integer 'n' as input and return
    a list of the first 'n' binary numbers.
    """

    from queue import Queue

    result = []
    if n <= 0:
        return result

    queue = Queue()
    # Enqueue the first binary number
    queue.put('1')

    for i in range(0, n):
        # Dequeue number
        current = queue.get()
        result.append(current)
        # Enqueue after adding 0 and 1
        for j in range(2):
            queue.put(current + str(j))

    return result


print(generate_binary_numbers(0))
print(generate_binary_numbers(1))
print(generate_binary_numbers(2))
print(generate_binary_numbers(6))
print(generate_binary_numbers(16))
