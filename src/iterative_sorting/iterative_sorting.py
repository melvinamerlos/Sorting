# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

# Loop through elements on right-hand-side of current index 
        for j in range(cur_index, len(arr)):
            rhs_cur_index = j
             # if (the value of the smallest_index is more than value of rhs_cur_index):
                # smallest value location is the rhs_cur_index at iteration j
            if arr[smallest_index] > arr[rhs_cur_index]:
                smallest_index = rhs_cur_index

        # TO-DO: swap
        # placeholder holds the smallest element in iteration i
        placeholder = arr[smallest_index]

        # swap the number at iteration j with number at iteration i
        arr[smallest_index] = arr[cur_index]

        # and vice-versa
        arr[cur_index] = placeholder

    print(arr)
    return arr

arr = [2,3,4,8,5]
selection_sort( arr )


# TO-DO: implement the Bubble Sort function below

def bubble_sort( arr ):
    # Loop through your array
    for i in range( 0, len( arr )-1 ):
        # Compare each element to its neighbor
        for j in range( 0, len( arr )-i-1 ):
            # If elements in wrong position (relative to each other, swap them)
            if ( arr[j] > arr[j+1] ):
                # The swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
    return arr

bubble_sort(arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr