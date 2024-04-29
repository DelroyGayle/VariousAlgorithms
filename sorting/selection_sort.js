
// JavaScript program for the implementation of selection sort
function swap(array,x_pointer, y_pointer) {
    let temp = array[x_pointer];
    array[x_pointer] = array[y_pointer];
    array[y_pointer] = temp;
}

function selectionSort(array,  n) {
    let i, j, min_index;

    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in unsorted array
        min_index = i;
        for (j = i + 1; j < n; j++) {
            if (array[j] < array[min_index]) {
                min_index = j;
            }
        }

        // Swap the found minimum element with the first element
        swap(array,min_index, i);
    }
}

function printArray(array) {
    console.log("Sorted array:");
    console.log(array.join(" "));
}

const array = [64, 25, 12, -3, -9, 22, 11];
const n = array.length;
selectionSort(array, n);
printArray(array);

/*

Output:

Sorted array:
-9 -3 11 12 22 25 64

*/