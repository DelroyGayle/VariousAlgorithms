def generate_octal_numbers(n):
    """
    Proof of concept:
    Generate 'n' octal numbers using the Python 'Queue' data structure
    That is, generate the first 'n' octal numbers
    The algorithm must take in an integer 'n' as input and return
    a list of the first 'n' octal numbers.
    """

    from queue import Queue

    result = []
    if n <= 0:
        return result

    queue = Queue()
    # Enqueue the first set of octal numbers
    [queue.put(str(suffix)) for suffix in range(1, 8)]

    while True:
        current = queue.get()
        result.append(current)
        [queue.put(current + str(suffix)) for suffix in range(0, 8)]

        n -= 1
        if n == 0:
            break

    return result


print(0, generate_octal_numbers(0))
print(1, generate_octal_numbers(1))
print(2, generate_octal_numbers(2))
print(8, generate_octal_numbers(8))
print(16, generate_octal_numbers(16))
print(22, generate_octal_numbers(22))
