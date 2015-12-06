#Question 1

#The input file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
#Your task is to compute the number of inversions in the file given, where the row of the file indicates the entry of an array.
#Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures. 

# merge sort two sorted lists into one sorted list, and count number of inversions #
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
       
# recursions #    
def sort_and_count(array):
    if len(array) < 2:
        return array, 0
    middle = len(array) / 2
    left,inv_left = sort_and_count(array[:middle])
    right,inv_right = sort_and_count(array[middle:])
    merged, count = merge_list(left,right)
    count += (inv_left + inv_right)
    return merged, count  
    #return count
  
## read in file ##
import os
direct= "file path"
raw_data= open(os.path.join(direct, "IntegerArray.txt"), "r")    

inputlist= []
for line in raw_data:
    inputlist.append(int(line))  

# count the number of inversions #  
merge_array, inversions= sort_and_count(inputlist)   
print inversions         
    
