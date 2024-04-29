# Counting Sort

Counting Sort is a *non-comparison-based* sorting algorithm that works well when there is limited range of input values. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted. The basic idea behind the **Counting Sort** is to count the frequency of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

## Complexity Analysis of Counting Sort:

### Time Complexity: O(N+M), where N and M are the size of inputArray[] and countArray[] respectively.
Worst-case: *O(N+M)*.
Average-case: *O(N+M)*.
Best-case: *O(N+M)*.
Auxiliary Space: *O(N+M)*, where N and M are the space taken by outputArray[] and countArray[] respectively.

## Advantages of Counting Sort:
+ Counting Sort generally performs faster than all comparison-based sorting algorithms, such as merge-sort and quick-sort, if the range of input is of the order of the number of input.
+ Counting Sort is easy to code
+ Counting Sort is *a stable algorithm*.

## Disadvantages of Counting Sort:
+ Counting Sort does not work on decimal values.
+ Counting Sort is inefficient if the range of values to be sorted is very large.
+ Counting Sort is not an *in-place* sorting algorithm. It uses extra space for sorting the array elements.

References:
+ https://www.geeksforgeeks.org/counting-sort/ 
+ https://en.wikipedia.org/wiki/Counting_sort 


# Heap Sort

In computer science, **heapsort** is a comparison-based sorting algorithm which can be thought of as "an implementation of *selection sort* using the right data structure." Like selection sort (see below), heapsort divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element from it and inserting it into the sorted region. Unlike selection sort, heapsort does not waste time with a linear-time scan of the unsorted region; rather, heapsort maintains the unsorted region in a *binary heap* data structure to efficiently find the largest element in each step.

Heapsort is an *in-place algorithm*, but it is *not a stable sort*.

## Heap Sort Algorithm

+ First convert the array into a binary heap data structure using heapify 
+ Then one by one, delete the root node of the *Max-heap* and replace it with the last node in the heap
+ Then heapify the root of the heap. 
+ Repeat this process until size of heap is greater than 1.

### Further breakdown of the algorithm
+ Build a heap from the given input array.
+ Repeat the following steps until the heap contains only one element:
+ + Swap the root element of the heap (which is the largest element) with the last element of the heap.
+ + Remove the last element of the heap (which is now in the correct position).
+ + Heapify the remaining elements of the heap.
+ The sorted array is obtained by reversing the order of the elements in the input array.

## Complexity Analysis of Heap Sort:
Time Complexity: *O(N log N)*
Auxiliary Space: *O(log n)*, due to the recursive call stack. However, auxiliary space can be *O(1)* for iterative implementation.

## Advantages of Heap Sort:

* Efficient Time Complexity: Heap Sort has a time complexity of *O(n log n)* in all cases. This makes it efficient for sorting large datasets. The *log n* factor comes from the height of the binary heap, and it ensures that the algorithm maintains good performance even with a large number of elements.

* Memory Usage: Memory usage can be minimal (by writing an iterative heapify() instead of a recursive one). So apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work.

* Simplicity:  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion.

## Disadvantages of Heap Sort:

* Unstable: Heap Sort is unstable. It might rearrange the relative order.
* Efficiency: Heap Sort is not very efficient when working with highly complex data. 

## What are the two phases of Heap Sort?

1. In the first phase, the array is converted into a max heap. And 
2. In the second phase, the highest element is removed (i.e., the one at the tree root) and the remaining elements are used to create a new max heap.

## Why is Heap Sort not stable?

The Heap Sort algorithm is not a stable algorithm because we swap array[i] with array[0] in heapSort() which might change the relative ordering of the equivalent keys.

References:
+ https://en.wikipedia.org/wiki/Heapsort 

+ https://www.geeksforgeeks.org/heap-sort/ 

+ https://www.programiz.com/dsa/heap-sort#google_vignette 


# Merge Sort

**Merge Sort** is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.
That is, the merge sort *divides the array into two halves, sorts each half, and then merges the sorted halves together.* 
This process is repeated until the entire array has been sorted.

## Complexity Analysis of Merge Sort:

### Time Complexity:
Best Case: *O(n log n)*, When the array is already sorted or nearly sorted.
Average Case: *O(n log n)*, When the array is randomly ordered.
Worst Case: *O(n log n)*, When the array is sorted in reverse order.
Space Complexity: *O(n)*, Additional space is required for the temporary array used during merging.

## Advantages of Merge Sort:
* Stability: Merge Sort is a *stable sorting algorithm*, which means it maintains the relative order of equal elements in the input array.
* Guaranteed worst-case performance: Merge Sort has a worst-case time complexity of *O(N logN)*, which means it performs well even on large datasets.
* Simple to implement: The divide-and-conquer approach is straightforward.

## Disadvantages of Merge Sort:
* Space complexity: Merge Sort requires additional memory to store the merged sub-arrays during the sorting process. 
* Not in-place: Merge Sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
 
References:
+ https://www.geeksforgeeks.org/merge-sort/ 
+ https://www.geeksforgeeks.org/python-program-for-merge-sort/ 


# Quick Sort

**QuickSort** is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

## How does QuickSort work?

The key process in QuickSort is the *partition()* function. The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and 
+ *put all smaller elements to the left of the pivot*, and 
+ *all greater elements to the right of the pivot.*

Partition is done recursively on each side of the pivot after the pivot is placed in its correct position and this finally sorts the array.

## Choice of Pivot:
There are many different choices for picking pivots for example, 

+ Always pick the first element as a pivot.
+ Always pick the last element as a pivot
+ Pick a random element as a pivot.
+ Pick the middle as the pivot.

## Partition Algorithm

Start from the leftmost element and keep track of the index of smaller (or equal) elements as i. While traversing, if we find a smaller element, we swap the current element with array[i]. Otherwise, we ignore the current element.

Note: QuickSort can be converted to an iterative version with the help of an auxiliary stack
Reference: https://www.geeksforgeeks.org/quick-sort/ 


# Radix Sort

In computer science, **Radix Sort** is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix. For elements with more than one significant digit, this bucketing process is repeated for each digit, while preserving the ordering of the prior step, until all digits have been considered. For this reason, Radix Sort has also been called Bucket Sort and Digital Sort.

Radix Sort can be applied to data that can be sorted lexicographically, be they integers, words, punch cards, playing cards, or the mail.

## Digit Order

Radix sorts can be implemented to start at either the most significant digit (MSD) or least significant digit (LSD).
For example, with 1234, one could start with 1 (MSD) or 4 (LSD).

LSD radix sorts typically use the following sorting order: short keys come before longer keys, and then keys of the same length are sorted lexicographically. This coincides with the normal order of integer representations, 
like the sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]. LSD sorts are generally *stable sorts*.

Reference: https://en.wikipedia.org/wiki/Radix_sort 


# Selection Sort

**Selection Sort** is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 

## Advantages of Selection Sort Algorithm
+ Simple and easy to understand.
+ Works well with small datasets.

## Disadvantages of the Selection Sort Algorithm
+ Selection sort has a time complexity of *O(n^2)* in the worst and average case.
+ Does not work well on large datasets.
+ Does not preserve the relative order of items with equal keys which means it is *not stable*.

Reference: https://www.geeksforgeeks.org/selection-sort/

# Stable Selection Sort

A sorting algorithm is said to be *stable* if two objects with equal or same keys appear in the same order in sorted output as they appear in the input array to be sorted.

*Any comparison based sorting algorithm which is not stable by nature can be modified to be stable by changing the key comparison operation so that the comparison of two keys considers position as a factor for objects with equal key or by tweaking it in a way such that its meaning doesn’t change and it becomes stable as well.*

Selection Sort works by finding the minimum element and then inserting it in its correct position by swapping with the element which is in the position of this minimum element. **This is what makes it unstable.**

Selection Sort can be made *Stable* if instead of swapping, the minimum element is placed in its position without swapping i.e. *by placing the number in its position by pushing every element one step forward (shift all elements to the right by 1)*. 


Reference: https://www.geeksforgeeks.org/stable-selection-sort/ 