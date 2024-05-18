# The maximum and minimum difference -- Challenge version

Source: [Challenge Version](https://www.codewars.com/kata/583c592928a0c0449d000099)

## Description:
Given two array of integers(arr1, arr2). Your task is to find a pair of numbers(an element in arr1, and another element in arr2), their difference is as big as possible(absolute value); Again, you should find a pair of numbers, their difference is as small as possible. Return the maximum and minimum difference values by an array: [  max difference,  min difference  ]

For example:

Given arr1 = [3,10,5], arr2 = [20,7,15,8]
should return [17,2] because 20 - 3 = 17, 10 - 8 = 2

## Note:
* arr1 and arr2 contains only integers(positive, negative or 0);
* arr1 and arr2 may have different lengths, they always has at least one element;

All inputs are valid.
**This is a challenge version, Please optimize your algorithm to avoid time out ;-)**

## About testcases
* Basic test: 5 testcases
* Random test1: 100 testcases, arr1 and arr2 contains 1-20 elements
* Random test2: 300 testcases, arr1 and arr2 contains **10000** elements

## Some Examples
maxAndMin([3,10,5],[20,7,15,8]) === [17,2]<br>
maxAndMin([3],[20]) === [17,17]<br>
maxAndMin([3,10,5],[3,10,5]) === [7,0]<br>
maxAndMin([1,2,3,4,5],[6,7,8,9,10]) === [9,1]


The 'challenge' is to use a *n log(n) time complexity* solution in order that<br>the program does *not* timeout within the duration given for Codewars tests

Codewars also offers a [simple version](https://www.codewars.com/kata/583c5469977933319f000403) of this problem where the arrays are much smaller

## My Approach - Decorate and MergeSort

As a proof of concept I chose to use the Merge Sort Algorithm which has a time complexity of *n log(n)*
1) Label array1 as 'A' - whilst labelling determine the largest and smallest values of array1
2) Label array2 as 'B' - whilst labelling determine the largest and smallest values of array2
3) Perform a Merge Sort: 
* During Comparison of two elements, where the labels differ denotes a value from array1 is being compared be array2.
* By labelling array1 as 'A' and array2 as 'B', when performing the merge sort of the elements', where the labels differ, check for a smaller minimum value
4) When the sort done, find the maximum of (Largest array1 value - Smallest array2 value) and (Largest array2 value - Smallest array1 value)
5) *max* and *min* has been determined