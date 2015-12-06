# programming-question-1
Algorithms: Design and Analysis Part 1

This is my python code for the programming questions in this course.


Question 1

The input file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the row of the file indicates the entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

Solution keys: 

1) For an array of size n, merge sort uses at most 6n(logn+1) operations;

2) The number of inversions is the number of pairs (i,j) of array indices i<j and A[i] > A[j];

3) We can recursively compute the number of inversions if the indices lie within one of two subarraies;

4) If the indices fall onto two subarraies, the split inversions involving an element of y in 2nd subarray C are the number of elements left in the 1st subarray B when y in copied to the sorted output D.

