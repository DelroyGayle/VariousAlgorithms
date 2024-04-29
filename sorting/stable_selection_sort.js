
// JavaScript program for the implementation of 
// a 'stable' version of the selection sort
function swap(array,x_pointer, y_pointer) {
    let temp = array[x_pointer];
    array[x_pointer] = array[y_pointer];
    array[y_pointer] = temp;
}

function stableSelectionSort(array,  n) {
 
    for (let i = 0; i < n - 1; i++) {
        // Find the minimum element from array[i] to array[n - 1]
        let minimum = i;
        for (j = i + 1; j < n; j++) {
            if (array[minimum] > array[j]) {
                minimum = j;
            }
        }

        // Move minimum element at current i towards the right.
        let minimum_key = array[minimum];
        while (minimum > i) 
        {
            array[minimum] = array[minimum - 1];
            minimum--;
        }
           
        array[i] = minimum_key;
    }
}

function printArray(array) {
    console.log("Sorted array:");
    console.log(array.join(" "));
}

const array = [64, 25, 12, -3, -9, 22, 11];
const n = array.length;
stableSelectionSort(array, n);
printArray(array);

/*

Output:

Sorted array:
-9 -3 11 12 22 25 64

*/