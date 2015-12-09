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


Question 3:

The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the row looks like : "6 155 56 52 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut (i.e., the minimum-possible number of crossing edges). (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) 

Solution keys:

1) A minimum cut problem is to compute a cut with fewest number of crossing edges;

2) The low success probability of one randomized contraction can be improved by repeated trials.



