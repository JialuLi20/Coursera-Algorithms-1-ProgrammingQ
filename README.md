Algorithms: Design and Analysis Part 1

This is my python code for the programming questions in this course.


Question 1:

The input file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the row of the file indicates the entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

Solution keys: 

1) For an array of size n, merge sort uses at most 6n(logn+1) operations;

2) The number of inversions is the number of pairs (i,j) of array indices i<j and ith element greater than jth element;

3) We can recursively compute the number of inversions if the indices lie within one of two subarraies;

4) If the indices fall onto two subarraies, the split inversions involving an element of y in 2nd subarray C are the number of elements left in the 1st subarray B when y in copied to the sorted output D.


Question 2:

The input file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the row of the file gives you the entry of an input array.
Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we will ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length, you should simply add to your running total of comparisons. (This is because the pivot element is compared to each of the other elements in the subarray in this recursive call.)

Solution keys: 

1) Given an array of size n, the average running time for Quick sort is O(nlogn).


