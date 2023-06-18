function mergesort(array) {
  // Base case: if the array has 0 or 1 element, it is already sorted
  if (array.length <= 1) {
    return array;
  }
  
  const mid = Math.floor(array.length / 2);
  const left = array.slice(0, mid);
  const right = array.slice(mid);
  
  mergesort(left);
  mergesort(right);
  
  let leftIndex = 0;
  let rightIndex = 0;
  let mergedIndex = 0;
  
  while (leftIndex < left.length && rightIndex < right.length) {
    // Compare and merge the elements from the left and right halves 
    if (left[leftIndex] < right[rightIndex]) {
      array[mergedIndex] = left[leftIndex];
      leftIndex++;
    } else {
      array[mergedIndex] = right[rightIndex];
      rightIndex++;
    }
    mergedIndex++;
  }
  
  while (leftIndex < left.length) {
    array[mergedIndex] = left[leftIndex];
    leftIndex++;
    mergedIndex++;
  }
  
  while (rightIndex < right.length) {
    array[mergedIndex] = right[rightIndex];
    rightIndex++;
    mergedIndex++;
  }
}

/* Time complexity analysis:
   The merge sort algorithm has a time complexity of O(n log n) in all cases.
   This is because the array is continuously divided in half until the base case is reached,
   and then the merging process takes place, which runs in linear time based on the size of the input.

   Space complexity analysis:
   The space complexity of the merge sort algorithm is O(n) due to the additional space required
   to store the divided halves during the recursion. However, the merge operation is done in-place
   without requiring additional space, which helps optimize memory usage. */
