from typing import List

def mergesort(array: List[int]) -> List[int]:
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively sort the left and right halves
    mergesort(left)  # Time complexity: O(n/2)
    mergesort(right)  # Time complexity: O(n/2)
    
    left_index = right_index = merged_index = 0
    while left_index < len(left) and right_index < len(right):
        # Compare and merge the elements from the left and right halves
        if left[left_index] < right[right_index]:
            array[merged_index] = left[left_index]
            left_index += 1
        else:
            array[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    # Copy the remaining elements from the left half, if any
    while left_index < len(left):
        array[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1

    # Copy the remaining elements from the right half, if any
    while right_index < len(right):
        array[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1

# Time complexity analysis:
# The merge sort algorithm has a time complexity of O(n log n) in all cases.
# This is because the array is continuously divided in half until the base case is reached,
# and then the merging process takes place, which runs in linear time based on the size of the input.

# Space complexity analysis:
# The space complexity of the merge sort algorithm is O(n) due to the additional space required
# to store the divided halves during the recursion. However, the merge operation is done in-place
# without requiring additional space, which helps optimize memory usage.
