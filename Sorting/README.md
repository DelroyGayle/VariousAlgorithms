Selection Sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 

**Advantages of Selection Sort Algorithm**
+ Simple and easy to understand.
+ Works well with small datasets.

**Disadvantages of the Selection Sort Algorithm**
+ Selection sort has a time complexity of O(n^2) in the worst and average case.
+ Does not work well on large datasets.
+ Does not preserve the relative order of items with equal keys which means it is not stable.

Reference: https://www.geeksforgeeks.org/selection-sort/

Stable Selection Sort

Stable Selection Sort

A sorting algorithm is said to be *stable* if two objects with equal or same keys appear in the same order in sorted output as they appear in the input array to be sorted.

*Any comparison based sorting algorithm which is not stable by nature can be modified to be stable by changing the key comparison operation so that the comparison of two keys considers position as a factor for objects with equal key or by tweaking it in a way such that its meaning doesn’t change and it becomes stable as well.*

Selection sort works by finding the minimum element and then inserting it in its correct position by swapping with the element which is in the position of this minimum element. **This is what makes it unstable.**

Selection sort can be made Stable if instead of swapping, the minimum element is placed in its position without swapping i.e. *by placing the number in its position by pushing every element one step forward (shift all elements to the right by 1)*. 


https://www.geeksforgeeks.org/stable-selection-sort/ 