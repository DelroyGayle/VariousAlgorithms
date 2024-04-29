// Function to partition the array and return the partition index
function partition(array, low, high) {
    // Choose the pivot
    // In this case, the last element
    let pivot = array[high];
  
    // Index of smaller element and indicates the correct position of pivot found so far
    let i = low - 1;
  
    for (let j = low; j <= high - 1; j++) {
        // If current element is smaller than the pivot
        if (array[j] < pivot) {
            // Increment index of smaller element
            i++;
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
    }
  
    [array[i + 1], array[high]] = [array[high], array[i + 1]]; // Swap pivot to its correct position
    return i + 1; // Return the partition index
}

// The main function that implements QuickSort
function quickSort(array, low, high) {
    if (low < high) {
        // partition_index is the partitioning index
        // array[partition_index] is now at the correct place
        let partition_index = partition(array, low, high);
  
        // Separately sort elements before partition and after partition
        quickSort(array, low, partition_index - 1);
        quickSort(array, partition_index + 1, high);
    }
}

// Driver code
let array = [10, 7, 8, 0, -2, 9, -8, 1, 5];
let N = array.length;

// Function call
quickSort(array, 0, N - 1);
console.log("Sorted array:");
console.log(array.join(" "));

/*

Output:

Sorted array:
-8 -2 0 1 5 7 8 9 10

Reference: https://www.geeksforgeeks.org/quick-sort/
*/