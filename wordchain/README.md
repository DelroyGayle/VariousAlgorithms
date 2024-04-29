Write a function longest_chain(words) that takes in a list of strings words and returns the longest possible word chain. A word chain is defined here as a list of words where the last letter of each word is the same as the first letter of its right neighbour.

Note — you can only use each word once in a word chain

For instance, apple elephant talk kite is a word chain

apple ends with e and elephant starts with e
elephant ends with t and talk starts with t
talk ends with k and kite starts with k
For instance, given a list of words:

```
words = ['apple', 'orange', 'eggplant', 'pear', 'hop', 'tooth', 'zaza']
longest_chain(words) should return:

['zaza', 'apple', 'eggplant', 'tooth', 'hop', 'pear']
Test your code on this:

words = [
    'apple', 'orange', 'pear', 'pineapple', 
    'durian', 'grapes', 'banana', 'kiwi',
    'dragonfruit', 'coconut', 'starfruit', 'strawberry',
    'acai', 'cherry', 'papaya', 'peach',
    'lychee', 'lemon', 'olive', 'tomato',
    'cherry tomato', 'elderberry', 'yuzu', 'avocado'
]

longest_chain(words)

['grapes', 'starfruit', 'tomato', 'orange', 'elderberry', 'yuzu']

```
[SOURCE](https://levelup.gitconnected.com/youre-a-python-king-if-you-can-answer-these-4-very-tricky-questions-207caa22cdee)
