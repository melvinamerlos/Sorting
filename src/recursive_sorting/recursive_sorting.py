# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a, b, i = 0, 0, 0 # counters for each array
    # while counter, 'a' AND 'b' is less than length of 'arrA' AND 'arrB', respectively do the following...
    while a < len(arrA) and b < len(arrB):
        # if value of item at index 'a' in 'arrA' is less than or equal to the value of the item in index 'b' of 'arrB'
        if arrA[a] <= arrB[b]:
            # then take the value that's in 'arrA', index 'a' and replace value of index 'i' in 'merged_arr'
            merged_arr[i] = arrA[a]
            a += 1 # and increment 'a'
        # otherwise if value of item at index 'a' in 'arrA' is NOT less than or equal to the value of the item in index 'b' of 'arrB'
        else:
            # then take the value that's in 'arrB', index 'b' and replace value of index 'i' in 'merged_arr'
            merged_arr[i] = arrB[b]
            b += 1 # and increment 'b'
        # increment i
        i += 1

    # while counter 'a' is less than length of 'arrA' do the following...
    while a < len(arrA):
        # replace value of index 'i' of 'merged_arr' with value of index 'a' in 'arrA'
        merged_arr[i] = arrA[a]
        a += 1 # increment
        i += 1
    # while counter 'b' is less than length of 'arrB' do the following...
    while b < len(arrB):
        # replace value of index 'i' of 'merged_arr' with value of index 'b' in 'arrB'
        merged_arr[i] = arrB[b]
        b += 1 # increment
        i += 1

    print("merge function:", merged_arr)
    return merged_arr

arr = [2, 3, 4, 8, 5]
arr2 = [22, 44, 88, 66, 88]

merge( arr, arr2 )

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if length of input is anything greater than 1..
    if len(arr) > 1:
        # determine midpoint
        mid = int(len(arr) / 2)
        # call recursively to split using midpoint
        lhs = merge_sort(arr[:mid])
        rhs = merge_sort(arr[mid:])
        # call merge(lhs,rhs) defined above
        arr = merge(lhs, rhs)

    print("merge_sort function:", arr)
    return arr

merge_sort( arr )

###########################################
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
