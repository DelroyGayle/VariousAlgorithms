# My attempts to solve Liu Zuo Lin's 20 Python Problems In ONE Line!
[Source](https://python.plainenglish.io/can-you-solve-these-20-python-problems-in-one-line-8e878a2c8b41)


# Disclaimer
# FOR FUN AND LAUGHTER ONLY. PLEASE DO NOT DO THIS IN PRODUCTION CODE!!! THANK YOU!

I attempted all the solutions nonetheless where possible I will also show Liu Zou Lin's own solutions
Liu Zuo Lin's 20 Problems are as follows:  

1) Factorial  
Write a function factorial(n) that takes in a positive integer n, and returns the product of 1 to n i.e. 1 * 2 * 3 * ... * n  

```
factorial(1)  # 1
factorial(2)  # 2
factorial(3)  # 6
factorial(4)  # 24
factorial(5)  # 120
```

2) Removing Vowels  
Write a function remove_vowels(string) that takes in a string, and returns another string with all vowels removed.  
Vowels refer to a, e, i, o & u.  

```
remove_vowels('apple')  # ppl
remove_vowels('orange') # rng
remove_vowels('pear')   # pr
```

3) Sum of Odd Numbers  
Write a function sum_odd(numberlist) that takes in a list of integers, and returns the sum of ONLY the odd numbers inside the list.

```
sum_odd([1,2,3,4,5])  # 9
sum_odd([1,2,3,4,6])  # 4
sum_odd([2,4,6,8,2])  # 0
sum_odd([1,1,1,1,1])  # 5
```

4) Filtering Numbers  
Write a function filter3(numberlist) that takes in a list of integers, and returns a new list containing only numbers that are divisible by 3.

```
filter3([1,2,3,4,5])    # [3]
filter3([1,3,8,9,12])   # [3,9,12]
filter3([3,3,5,6,6])    # [3,3,6,6]
```

5) Odd Even Labelling  
Write a function label(numberlist) that takes in a list of integers, and returns a new list containing 1 label for each integer. If the integer is odd, it is replaced with an 'odd' label, and vice versa for even numbers.

```
label([1,2,3,4,5])    # ['odd', 'even', 'odd', 'even', 'odd']
label([1,1,1,2,2])    # ['odd', 'odd', 'odd', 'even', 'even']
label([1,2,2,2,7])    # ['odd', 'even', 'even', 'even', 'odd']
```

6) Christmas Tree  
Write a function christmas_tree(n) that takes in a positive integer n (assume n is at least 2), and prints a christmas tree pattern of height n.  
Note that the trunk of the tree will always have a height of 2.

```
christmas_tree(3)

    *
   ***
  *****
    *
    *

christmas_tree(5)

    *
   ***
  *****
 *******
*********
    *
    *
```

7) Fibonacci Numbers
Fibonacci numbers are a series of numbers:  
That start with 0 and 1  
Where each new number is the sum of the previous 2 numbers.  
It goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …  
Write a function fib(n) that takes in a positive integer, and returns the nth fibonacci number.  

```
fib(1)  # 0
fib(2)  # 1
fib(3)  # 1
fib(4)  # 2
fib(5)  # 3
fib(6)  # 5
fib(7)  # 8
fib(8)  # 13
fib(9)  # 21
fib(10) # 34
```

8) Counting Fruits  
Write a function count_fruits(fruits) that takes in a list of strings fruits, and returns a dictionary containing each fruit’s counts.  
fruits = ['apple', 'apple', 'orange', 'apple', 'pear']  

```
count_fruits(fruits)


{'apple':3, 'orange':1, 'pear':1}
```

9) Combining Lists  
Write a function combine(list1, list2) that takes in 2 lists of strings, and returns a resultant list combining both.  
list1 = ['apple', 'orange']  
list2 = ['pie', 'juice']  

```
combine(list1, list2)

['apple pie', 'apple juice', 'orange pie', 'orange juice']*
```

10) Total cost of fruits  
You are given a list containing some information about fruits  
```
fruits = [
 {'name': 'apple', 'price':4, 'quantity':100},
 {'name': 'orange', 'price':5, 'quantity':100},
 {'name': 'pear', 'price':6, 'quantity':100},
]
```

Write a function total_cost(fruits) that takes in such a list, and calculates the total cost of fruits inside the list (price * quantity).

```
total_cost(fruits) # 1500*
```

11) Letter Pyramid  
Write a function pyramid(string) that takes in a string (assuming no spaces) and prints the following pattern.  
If the string is not long enough, add * characters behind.  

```
pyramid('abcdefg')

a
bc
def
g***


pyramid('abcdefghijkl')

a
bc
def
ghij
kl***

pyramid('abcdefghijklmno')


a
bc
def
ghij
klmno
```

12) Product Of List Of Numbers  
Write a function product(numberlist) that takes in a list of numbers, and multiplies all the numbers together. 
``` 
product([1,2,3,4,5])    # 120  
product([1,1,1,1,5])    # 5  
product([1,0,1,9,8])    # 0  
```

13) Sum Of Numbers In Nested List  
You are given a nested list of numbers. Assume that it can have any level of nesting.  
Write a function sum_nested(nlist) that takes in this nested list, and returns the sum of all numbers.  
```
nlist = [1, [2, [[[3]]]], [4, [5, 6, [7]]], 8, [[9]], 10]

sum_nested(nlist)
```

14) Number of Holes  
You are given a list of zeros and ones. Zeros represent hole, while ones represent filled spaces.  
Multiple zeros in a row make up 1 hole, no matter how many zeros there are.  
Write a function count_holes(list) that takes in such a list, and counts the total number of holes.  
```
count_holes([1,0,0,0,1,1,1,1,1])    # 1
count_holes([1,0,0,0,1,1,0,0,1])    # 2
count_holes([1,0,1,0,1,0,1,0,1])    # 4
```

15) Splitting CamelCase Strings  
CamelCase is the practice of writing phrases without using spaces,   
but capitalizing the first letter of each individual word to separate the words.  
Here are some examples of CamelCase strings:  
```
MyNameIsRocky
IAmHappy
AppleOrangePear


Write a function split_camel(string) that takes in a valid CamelCase string, and splits it into individual words.
split_camel('MyNameIsRocky')    # ['My', 'Name', 'Is', 'Rocky']
split_camel('IAmHappy')         # ['I', 'Am', 'Happy']
split_camel('AppleOrangePear')  # ['Apple', 'Orange', 'Pear']
```

16) Highest Common Factor  
The highest common factor of 2 numbers is the largest possible integer that both numbers are divisible by.  
Write a function hcf(a,b) that takes in 2 numbers a and b, and returns the highest common factor of a and b.  
```
hcf(8, 12)   # 4
hcf(20, 30)  # 10
hcf(7, 15)   # 1
hcf(50,100)  # 50
```

17) Checking If Maze Is Solvable  
You are given mazes (2D lists) like these:  
```
maze1 = [
   "S-#--",
   "-#---",
   "-#-#-",
   "---#X"
]
```

```
maze2 = [
   "S----",
   "-#--#",
   "---#-",
   "-#-#X"
]
```

* The S character represents the starting point of the player.
* The X character represents the objective
* The \- characters represent roads, which the player can walk on
* The \# characters represent walls, which the player cannot walk on
* The player needs to reach the object X from S
* S will always be at the topmost, leftmost coordinate, but X can be anywhere.
* The player can only move horizontally and vertically, one step at a go.


Write a function is_solvable(maze) that takes in a maze, and returns True if the maze if solvable and False otherwise.  
A maze is solvable if it is possible for the player to get to X from S.  

![image](https://github.com/DelroyGayle/VariousAlgorithms/assets/91061592/67187656-5060-430a-8c1a-b43429463fdd)


18) Checking For Prime Numbers  
A prime number is a positive integer larger than 1 that is divisible ONLY by 1 and itself.<br> Some examples of prime numbers:<br>
2 3 5 7 11 13 17 19 23 29 ...  

Write a function is_prime(n) that takes in a positive integer, and returns True if n is a prime number, and False otherwise.  

```
is_prime(2)    # True
is_prime(3)    # True
is_prime(4)    # False
is_prime(5)    # True
is_prime(6)    # False
is_prime(7)    # True
is_prime(8)    # False
is_prime(9)    # False
is_prime(10)   # False
is_prime(11)   # True
is_prime(12)   # False
is_prime(13)   # True
is_prime(14)   # False
is_prime(15)   # False
is_prime(16)   # False
is_prime(17)   # True
is_prime(18)   # False
is_prime(19)   # True
is_prime(20)   # False

```

19) Aligning Strings By Letter  

strings = ["apple", "orange", "pear", "pineapple", "durian"]  
letter = "e"  
You are given a list of words, and a letter. Write a function align(strings, letter) that prints this pattern which aligns the letter in all words. Ignore words that do not contain letter.  
align(strings, 'e')  

```
# this prints the pattern:

    apple
   orange
       pear
     pineapple

# notice all the letter e are aligned vertically
# durian does not contain e, so it's not even printed



align(strings, 'a')

# this prints the pattern:

       apple
     orange
     pear
   pineapple
   durian

# notice all the letter are aligned vertically
```

20) Extracting Key From Messy Dictionary  
You are given a messy data structure with multiple levels of nesting.  
```
data = {
   "type": "video",
   "videoID": "vid001",
   "links": [
       {"type":"video", "videoID":"vid002", "links":[]},
       {   "type":"video",
           "videoID":"vid003",
           "links": [
           {"type": "video", "videoID":"vid004"},
           {"type": "video", "videoID":"vid005"},
           ]
       },
       {"type":"video", "videoID":"vid006"},
       {   "type":"video",
           "videoID":"vid007",
           "links": [
           {"type":"video", "videoID":"vid008", "links": [
               {   "type":"video",
                   "videoID":"vid009",
                   "links": [{"type":"video", "videoID":"vid010"}]
               }
           ]}
       ]},
   ]
}
```

Write a function extract(data, key) that takes in this messy data structure data, and a string key.  
This function then extracts ALL values with the key key inside the messy data structure, and returns them in a list.  
extract(data, 'videoID')

```
['vid001', 'vid002', 'vid003', 'vid004', 'vid005',
 'vid006', 'vid007', 'vid008', 'vid009', 'vid010']
```


# My Approach

The general approach I took was 
1. to write a solution in JavaScript first.
2. Convert the program to a Python version
3. Convert the Python program to one line using semicolons


Therefore, generally there will be both JavaScript and Python solutions to each challenge.