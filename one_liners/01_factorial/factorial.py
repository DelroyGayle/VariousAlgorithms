"""
1) Factorial  
Write a function factorial(n) that takes in a positive integer n, 
and returns the product of 1 to n i.e. 1 * 2 * 3 * ... * n

```
factorial(1)  # 1
factorial(2)  # 2
factorial(3)  # 6
factorial(4)  # 24
factorial(5)  # 120
```
"""

# VERSION 1

from functools import reduce

n = 100
# THE ONE-LINER
factorial1 = reduce(lambda x, y: x * y, range(1, n+1))
# THE RESULT
print(factorial1)

"""
9332621544394415268169923885626670049071596826438162146859296389521
7599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
"""

def factorial2(n):
    if n == 1:
        return 1

    return n * factorial2(n-1)

result = factorial2(5)
print(result)  # 120

# Here is a one liner recursive solution I found on Stack Overflow
# https://stackoverflow.com/questions/51777932/writing-a-factorial-function-in-one-line-in-python
factorial3 = lambda x : x and x * factorial3(x - 1) or 1

result = factorial3(8)
print(result)  # 40320

"""
# Experiment with List Comprehension
# Generate a list of numbers e.g. up to 8 ==> [0, 1, 2, ... 8]
print(list(range(9))) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(list(range(1, 9))) # [1, 2, 3, 4, 5, 6, 7, 8]
print(list(enumerate(list(range(1, 9))))) # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
"""


"""
Therefore, using List Comprehension,
generate a Cumulative Products list  and return the final answer:
i.e. [1, 2, 6, 24, 120, 720, ...]
"""

# My One Liner
def factorial_oneliner(x): numbers=list(range(1,x+2)); product=[1];return [product.append(product[0]*n) or product.pop(0) for n in numbers][-1]
print(factorial_oneliner(1))
print(factorial_oneliner(5))
print(factorial_oneliner(10))
print(factorial_oneliner(100))

"""
Output:

1
120
3628800
933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208
27223758251185210916864000000000000000000000000

Another solution using the walrus operator:
"""

def factorial_oneliner_2(x): numbers=list(range(1,x+1)); product=1; return [product := product * each_number for each_number in numbers][-1]
print(factorial_oneliner_2(1))
print(factorial_oneliner_2(2))
print(factorial_oneliner_2(3))
print(factorial_oneliner_2(5))
print(factorial_oneliner_2(10))

"""
Output:

1
2
6
120
3628800
"""

