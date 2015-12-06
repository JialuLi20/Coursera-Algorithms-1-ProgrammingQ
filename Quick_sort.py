
# Quick sort using first element as the pivot 

def partition(A, l, r):
    p= A[l] # use first element as the pivot #
    i= l+1
    for j in range((l+1), r):
        if A[j]< p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l] 
    
    return i-1
          
                
def quick_sort(A, l, r):
    if l < r:
        newpivotindex = partition(A, l, r)
        quick_sort(A, l, newpivotindex)
        quick_sort(A, newpivotindex+1, r)
        
    return A
        
