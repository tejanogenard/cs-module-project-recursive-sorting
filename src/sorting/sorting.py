# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    for n in arrA and arrB:
        if arrA[n] > arrB[n]:
            merged_arr.append(arrB[n])
            merged_arr.append(arrA[n])

        elif arrB[n] > arrA[n]:
            merged_arr.append(arrA[n])
            merged_arr.append(arrB[n])


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # recursively call merge_sort() on LHS
    # recursively call merge_sort() on RHS
    # merge sorted pieces
    if len(arr)>1: 
        m = len(arr)//2
        left = arr[:m] 
        right = arr[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        arr =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                arr.append(left[0]) 
                left.pop(0) 
            else: 
                arr.append(right[0]) 
                right.pop(0) 


    #append 
        for i in left: 
            arr.append(i) 
        for i in right: 
            arr.append(i) 
                  
    return arr 


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
