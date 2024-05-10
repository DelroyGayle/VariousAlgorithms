def generate_octal_numbers(n):
    """
    Proof of concept:
    Generate 'n' octal numbers using a 'queue'
    That is, generate the first 'n' octal numbers
    The algorithm must take in an integer 'n' as input and return
    a list of the first 'n' octal numbers.
    """

    result = []
    if n <= 0:
        return result
    # if n == 1:
    #     return ['1']

    queue = ['1']
    queue = [str(suffix) for suffix in range(1, 8)]
    while True:
        current = queue.pop(0)
        result.append(current)
        queue += ([current + str(suffix) for suffix in range(0, 8)])

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
