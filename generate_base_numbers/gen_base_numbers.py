from queue import Queue
import string
import pprint

RANGE_0_TO_10 = [str(digit) for digit in range(0, 10)]
RANGE_0_TO_36 = RANGE_0_TO_10 + list(string.ascii_uppercase)


def generate_base_numbers(base, n):
    """
    Proof of concept:
    Generate 'n' numbers in a given base using
    the Python 'Queue' data structure

    Base number must be between 2 and 36
    'n' must be greater than 0

    The algorithm must take in an integer 'n' as input and return
    a list of the first 'n' numbers in the given base.
    """

    if not (isinstance(base, int) and base >= 2 and base <= 36):
        print("Illegal Base Number: Must be an integer "
              "between 2 and 36 inclusive")
        return None

    if not (isinstance(n, int) and n > 0):
        print("Illegal 'n': Must be an integer greater than 0")
        return None

    result = []
    if n <= 0:
        return result

    queue = Queue()
    #  Enqueue the first set of numbers within the base
    #  beginning with 1
    queue_range(queue, base, current='', begin_with=1)

    while True:
        current = queue.get()
        result.append(current)
        queue_range(queue, base, current)

        n -= 1
        if n == 0:
            break

    return result


def queue_range(queue, base, current='', begin_with=0):
    """
    Queue a range of values for a particular base number
    """

    if base <= 10:
        [queue.put(current + RANGE_0_TO_10[suffix])
            for suffix in range(begin_with, base)]
        return

    # Handle letters A-Z for base 11 upwards
    [queue.put(current + RANGE_0_TO_36[suffix])
        for suffix in range(begin_with, base)]


print(generate_base_numbers('', ''))
print(generate_base_numbers(0, 6))
print(generate_base_numbers(37, 6))
print(generate_base_numbers(2, 0))
print("")
print(2, 1, generate_base_numbers(2, 1))
print(2, 2, generate_base_numbers(2, 2))
print(2, 6, generate_base_numbers(2, 6))
print(2, 16, generate_base_numbers(2, 16))
print(3, 16, generate_base_numbers(3, 16))
print(5, 16, generate_base_numbers(5, 16))
print(16, 16, generate_base_numbers(16, 16))
print("")
print("Base 16 n= 40")
pprint.pp(generate_base_numbers(16, 40), width=60, compact=True)
print("")
print("Base 36 n= 35")
pprint.pp(generate_base_numbers(36, 35), width=60, compact=True)
print("")
print("Base 36 n= 40")
pprint.pp(generate_base_numbers(36, 40), width=60, compact=True)
print("")
print("Base 36 n= 72")
pprint.pp(generate_base_numbers(36, 72), width=60, compact=True)


"""
Output:

Illegal Base Number: Must be an integer between 2 and 36 inclusive
None
Illegal Base Number: Must be an integer between 2 and 36 inclusive
None
Illegal Base Number: Must be an integer between 2 and 36 inclusive
None
Illegal 'n': Must be an integer greater than 0
None

2 1 ['1']
2 2 ['1', '10']
2 6 ['1', '10', '11', '100', '101', '110']
2 16 ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010',
      '1011', '1100', '1101', '1110', '1111', '10000']
3 16 ['1', '2', '10', '11', '12', '20', '21', '22', '100', '101', '102',
     '110', '111', '112', '120', '121']
5 16 ['1', '2', '3', '4', '10', '11', '12', '13', '14', '20', '21', '22', '23',
      '24', '30', '31']
16 16 ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
       'E', 'F', '10']

Base 16 n= 40
['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
 'D', 'E', 'F', '10', '11', '12', '13', '14', '15', '16',
 '17', '18', '19', '1A', '1B', '1C', '1D', '1E', '1F', '20',
 '21', '22', '23', '24', '25', '26', '27', '28']

Base 36 n= 35
['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Base 36 n= 40
['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 '10', '11', '12', '13', '14']

Base 36 n= 72
['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
 '1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', '1I', '1J',
 '1K', '1L', '1M', '1N', '1O', '1P', '1Q', '1R', '1S', '1T',
 '1U', '1V', '1W', '1X', '1Y', '1Z', '20']
"""
