function insertionSort(array) {
  /*
  Sorts the given array using the insertion sort algorithm.

  Running time: O(n^2) in the worst case

  Parameters:
  - array: The array to be sorted.

  Returns:
  A sorted version of the array.
  */
  const length = array.length;

  if (length <= 1) {
    return array;
  }

  for (let i = 1; i < length; i++) {
    const key = array[i];
    let j = i - 1;

    while (j >= 0 && array[j] > key) {
      array[j + 1] = array[j];
      j--;
    }

    array[j + 1] = key;
  }

  return array;
}
