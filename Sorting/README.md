# Counting Sort

Counting Sort is a *non-comparison-based* sorting algorithm that works well when there is limited range of input values. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted. The basic idea behind the **Counting Sort** is to count the frequency of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

## Complexity Analysis of Counting Sort:

### Time Complexity: O(N+M), where N and M are the size of inputArray[] and countArray[] respectively.
Worst-case: O(N+M).
Average-case: O(N+M).
Best-case: O(N+M).
Auxiliary Space: O(N+M), where N and M are the space taken by outputArray[] and countArray[] respectively.

## Advantages of Counting Sort:
+ Counting sort generally performs faster than all comparison-based sorting algorithms, such as merge sort and quicksort, if the range of input is of the order of the number of input.
+ Counting sort is easy to code
+ Counting sort is a stable algorithm.

## Disadvantages of Counting Sort:
+ Counting sort does not work on decimal values.
+ Counting sort is inefficient if the range of values to be sorted is very large.
+ Counting sort is not an *in-place* sorting algorithm. It uses extra space for sorting the array elements.

References:
+ https://www.geeksforgeeks.org/counting-sort/ 
+ https://en.wikipedia.org/wiki/Counting_sort 

# Merge Sort

Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.
That is, the merge sort *divides the array into two halves, sorts each half, and then merge the sorted halves together.* 
This process is repeated until the entire array has been sorted.

## Complexity Analysis of Merge Sort:

### Time Complexity:

Best Case: O(n log n), When the array is already sorted or nearly sorted.
Average Case: O(n log n), When the array is randomly ordered.
Worst Case: O(n log n), When the array is sorted in reverse order.
Space Complexity: O(n), Additional space is required for the temporary array used during merging.

## Advantages of Merge Sort:
* Stability: Merge sort is a *stable sorting algorithm*, which means it maintains the relative order of equal elements in the input array.
* Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.
* Simple to implement: The divide-and-conquer approach is straightforward.

## Disadvantages of Merge Sort:
* Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process. 
* Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
 
References:
+ https://www.geeksforgeeks.org/merge-sort/ 
+ https://www.geeksforgeeks.org/python-program-for-merge-sort/ 

# Quick Sort

QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

## How does QuickSort work?

The key process in quickSort is the *partition()* function. The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and 
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

Start from the leftmost element and keep track of the index of smaller (or equal) elements as i. While traversing, if we find a smaller element, we swap the current element with arr[i]. Otherwise, we ignore the current element.

Reference: https://www.geeksforgeeks.org/quick-sort/ 

# Selection Sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 

## Advantages of Selection Sort Algorithm
+ Simple and easy to understand.
+ Works well with small datasets.

## Disadvantages of the Selection Sort Algorithm
+ Selection sort has a time complexity of O(n^2) in the worst and average case.
+ Does not work well on large datasets.
+ Does not preserve the relative order of items with equal keys which means it is not stable.

Reference: https://www.geeksforgeeks.org/selection-sort/

# Stable Selection Sort

A sorting algorithm is said to be *stable* if two objects with equal or same keys appear in the same order in sorted output as they appear in the input array to be sorted.

*Any comparison based sorting algorithm which is not stable by nature can be modified to be stable by changing the key comparison operation so that the comparison of two keys considers position as a factor for objects with equal key or by tweaking it in a way such that its meaning doesn’t change and it becomes stable as well.*

Selection sort works by finding the minimum element and then inserting it in its correct position by swapping with the element which is in the position of this minimum element. **This is what makes it unstable.**

Selection sort can be made Stable if instead of swapping, the minimum element is placed in its position without swapping i.e. *by placing the number in its position by pushing every element one step forward (shift all elements to the right by 1)*. 


Reference: https://www.geeksforgeeks.org/stable-selection-sort/ 