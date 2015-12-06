
# Partition around first element #
#l: leftmost index;
#r: length of the array.
def partition_first(A, l, r):
    p= A[l] # use first element as the pivot #
    i= l+1
    for j in range((l+1), r):
        if A[j]< p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l] 
    
    return i-1
    
# Count the number of comparisons #
comparison= 0
def quicksort_first(A, l, r):
    global comparison
    if l < r:
        newpivotindex = partition_first(A, l, r)
        comparison += (r - l - 1)
        quicksort_first(A, l, newpivotindex) 
        quicksort_first(A, newpivotindex+1, r)
    
    return comparison   
        
        
        
# Partition around last element #
def partition_last(A, l, r):
    p= A[r-1] # use last element as the pivot #
    A[l], A[r-1]= A[r-1], A[l] # swap the position of first and last element #
    i= l+1
    for j in range((l+1), r):
        if A[j]< p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l] 
    
    return i-1
    
# Count the number of comparisons #
comparison= 0
def quicksort_last(A, l, r):
    global comparison
    if l < r:
        newpivotindex = partition_last(A, l, r)
        comparison += (r - l - 1)
        quicksort_last(A, l, newpivotindex) 
        quicksort_last(A, newpivotindex+1, r)
    
    return comparison   
   
