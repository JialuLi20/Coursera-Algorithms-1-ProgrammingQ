# Merge sort #

# merge and sort two sorted lists into one sorted list #
def merge_list(A, B):
    result=[]
    i,j = 0,0
    nA, nB= len(A), len(B)
    while i < nA and j < nB:
        if A[i] < B[j]:
            result.append(A[i])
            i+=1
        elif A[i] > B[j]:
            result.append(B[j])
            j+=1
        elif A[i] == B[j]:
            result.append(A[i])
            i+=1
            j+=1        
    result=result + A[i:]
    result=result + B[j:]
    return result
    
# recursively merge sort #
def merge_sort(array):
    if len(array) < 2:
        return array
    middle = len(array) / 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    merged= merge_list(left,right)
    return merged
