def insertionSort(array):
    """
    Sorts the given array using the insertion sort algorithm.
    Running time: O(n^2) in the worst case
    Parameters:
    - array: The array to be sorted.

    Returns:
    A sorted version of the array.
    """
    length = len(array)
    if length <= 1:
        return array

    for index in range(1, length):
        key = array[index]
        j = index - 1
        
        # Move elements greater than key to the right
        # to find the correct position for key
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        # Insert key at the appropriate position
        array[j + 1] = key
    
    return array
    
    
