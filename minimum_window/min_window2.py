# My solution to Minimum Window Substring
# Returns a list of all possible solutions

from collections import Counter
import sys

def contains_all(haystack, needle, needle_counter): 
  haystack_counter = Counter(haystack)
  return all(haystack_counter[c] >= needle_counter[c] for c in needle)
  

def constraint_satisfied(thewindow_string, 
                         minimum_window_size, 
                         minimum_window):
  """
  Found a window which satisfies the constraint
  Is it shorter?
  """

  global all_solutions

  the_length = len(thewindow_string)
  if the_length < minimum_window_size:
    # Yes. Found Better Solution
    minimum_window_size = the_length
    minimum_window = thewindow_string
    all_solutions = [ minimum_window ]

  elif the_length == minimum_window_size:

    all_solutions.append(thewindow_string)
    
  return (minimum_window_size, minimum_window)


def find_window(searchString, constraint):
  """
  :type searchString: str
  :type constraint: str
  :rtype: str
  """
  
  global all_solutions

  all_solutions = []
  n = len(searchString)
  if n == 0:
    return all_solutions
        
  # It contains the min length seen so far
  minimum_window_size = sys.maxsize
        
  # It contains the minimum length substring
  minimum_window = ""
  
  # It contains the number of each character
  constraint_counter = Counter(constraint)
  left = 0
  
  for right in range(left, n):
    thewindow_string = searchString[left: right + 1]
    if not contains_all(thewindow_string, constraint, constraint_counter):
      # Does not satisfy - continue search
      continue
  
    # Found a window which satisfies the constraint
    # Is it shorter?
    minimum_window_size, minimum_window = constraint_satisfied(thewindow_string, 
                                                               minimum_window_size, 
                                                               minimum_window)

    # Now contract the window to see if there is another solution
    
    for left in range(left + 1, right + 1):
      thewindow_string = searchString[left: right + 1]
      if not contains_all(thewindow_string, constraint, constraint_counter):
      # No longer satisfies the constraint - end the inner loop
        break

      # Found a window which satisfies the constraint
      # Is it shorter?
      minimum_window_size, minimum_window = constraint_satisfied(thewindow_string, 
                                                                 minimum_window_size, 
                                                                 minimum_window)

  return all_solutions

print(find_window("abcd", "abcd")) # abcd
print(find_window("abcd", "d")) # d
print(find_window("azjskfzts", "sz")) # zjs
print(find_window("ADOBECODEBANC", "ABC")) # BANC
print(find_window("abcdef", "abcdef")) # abcdef
print(find_window("donutsandwafflemakemehungry", "flea")) # affle
print(find_window("whoopiepiesmakemyscalegroan", "roam")) # myscalegro
print(find_window("coffeeteabiscuits", "cake")) # "" NO SOLUTION

"""
OUTPUT

['abcd']
['d']
['zjs', 'zts']
['BANC']
['abcdef']
['affle', 'flema']
['myscalegro']
[]
"""