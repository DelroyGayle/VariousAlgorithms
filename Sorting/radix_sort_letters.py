"""
Radix Sort of words - Least significant digit (LSD) approach
Proof of Concept in regards to sorting
a list of words using Radix 26

However need a NULL character to act as a NON-LETTER character
So in fact, I have to use Radix 27
That is,
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
   a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
"""

RADIX = 27
ASCII_A = 97 # ASCII Code for 'a'

def radix_word_sort(array):
    arraysize = len(array)

    # Determine the length of the longest word
    longest = len(max(array, key=len))

    pass_number = 1
    # The number of letters of the longest word
    # is the number of passes
    for _ in range(longest):
        bucket = [[] for _ in range(RADIX)]
        for i in range(arraysize):
            bucket_number = 0 # Default

            """
            First Calculation:
            Take the length of the longest word e.g. 'computer' = 8 
            Subtract the length of the current word from the longest value
            If the absolute value of the current subscript
            is <= the difference then it is a space i.e. place in bucket 0
            For example, the word 'cat' is length 3
            8-3 = 5
            So if the difference is either -1, -2, -3, -4 or -5
            The character used is SPACE which is the NULL value
            """
            the_length = len(array[i])
            difference = longest - the_length
            if difference != 0 and pass_number <= difference:
                pass
            else:
                """
                Second Calculation: Need to determine the correct index
                to determine the letter for the current word

                Using the word 'cat'

                c a t
                0 1 2

                Pass Number = 1
                Index = 3 - 1 = 2
                Letter 't'

                Pass Number = 2
                Index = 3 - 2 = 1
                Letter 'a'

                Pass Number = 3
                Index = 3 - 3 = 0
                Letter 'c'
                """

                the_word = array[i]
                the_index = longest - pass_number
                letter = the_word[the_index]
                bucket_number = ord(letter) - ASCII_A + 1

            # Place word into the appropriate bucket
            bucket[bucket_number].append(array[i])          

        array = []
        for i in range(RADIX):
            array.extend(bucket[i])
        # Proceed to the next letter
        pass_number += 1

    # Loop completed which means the array is now sorted!

    return array

# A list of 20 random words
word_list = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
             "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"] 
sorted = radix_word_sort(word_list) 
print("Sorted word list is:") 
print(sorted) 

word_list = ["gostion", "ovessy", "bandal", "shoption", "repatity", "whiver",
             "o", "phydry", "zebra", "victor", "yes", "no", "queen", "king",
             "unicorn", "snodrocash", 
             "totent", "pookeratry", "hummist", "xray"]
sorted = radix_word_sort(word_list) 
print("Sorted word list is:") 
print(sorted) 
"""
Output:

Sorted word list is:
['apple', 'book', 'car', 'cat', 'chair', 'computer', 'desk', 'dog', 'door', 
 'floor', 'house', 'keyboard', 'laptop', 'mouse', 'pen', 'phone', 'table', 
 'tree', 'wall', 'window']
Sorted word list is:
['bandal', 'gostion', 'hummist', 'king', 'no', 'o', 'ovessy', 'phydry', 
 'pookeratry', 'queen', 'repatity', 'shoption', 'snodrocash', 'totent', 
 'unicorn', 'victor', 'whiver', 'xray', 'yes', 'zebra']
"""