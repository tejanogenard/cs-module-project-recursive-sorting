# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    if end >= start:

        middle = (end + start) // 2 

        #check to see if the middle is equal to the target 
        if arr[middle] == target:
            return middle 

        #check if target is greater
        elif target > arr[middle]:
            return binary_search(arr, target, middle + 1, end)

        #else target is lesser
        elif arr[middle] > target: 
            return binary_search(arr, target, start, middle - 1)
        
        #else target is not found 
    else: 
        return -1 

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

