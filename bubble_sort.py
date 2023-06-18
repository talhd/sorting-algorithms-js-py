def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already sorted
        
        # Traverse the array from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr
