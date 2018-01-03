# Searches


### Explanation

Take an array of entities consisting of two fields: a student name (string) and a grade (integer). An example of this array is:

Array 1: [(Matthew, 4), (John, 9), (Mark, 8),(Luke, 6)]

In this case the data may be sorted by either the name or the grade value. By increasingly sorting by name, the result is:

Array 2: [(John, 9), (Luke, 6), (Mark, 8), (Matthew, 4)]

On the other hand by increasingly sorting by the grade value you get:

Array 3: [(John, 9), (Mark, 8), (Luke, 6), (Matthew, 4)]

Consider Array 1 above. Each entity has a characteristic whose values can be ordered, that is to say, there exists a relation of total ordering on the set of these values. This characteristic is called the sorting key. In this case there are two possible sorting keys. Array 2 shows the ordering when the student name is the key and Array 3 shows the ordering where the grade is the key. In both cases, either lexicographically or numerically, the array is deemed to be sorted.

But alas, sorting in the real world is never this simplistic. Often real world sorting problems tend to deal with thousands of elements at a time. Sorting a large number of elements can take a substantial amount of computing resources. Therefore the sorting problem is primarily concerned with using less resources during the sorting process.

To reiterate, Sorting is a fundamental algorithmic problem in computer science. The sorting problem refers to rearranging the elements of the set such that the values of the key are in a given order (an increasing or a decreasing order). There are many, many sorting algorithms that have been developed and analysed with the view to doing just this while also using less computing resources.

Some properties of these aforementioned algorithms are simplicity, stability, naturalness and efficiency. Essentially, you have a good sorting algorithm if it is intuitive and easy to understand, preserves the relative order of any two equal elements in its input, requires fewer operations as the distance between the initial and sorted arrays decrease, doesn’t require a large amount of resources.

Some algorithms do some of these things better than others. At the end of the day, you'll find that each sorting problem can be different, and that it's important to know what sorting algorithm best fits each kind of problem. Some sorts work better on nearly-sorted datasets, some sorts have less initial overhead, and some sorts have better worst-case time complexities than others. Simply put, there is no "ideal" sorting algorithm that suits all sorting problems because there is no "ideal" sorting problem.

The only ideal sorting algorithm is the one which best solves the sorting problem your confronted with, and to write and implementation a solution to the problem, it's vital you have previous knowledge of sorting algorithms.



### Bubble Sort

#### Explanation

Bubble sort algorithm starts by comparing the first two elements of a given sequence and swapping if one is found to be a larger value. Then, second and third elements are compared and swapped if it is necessary and this process go on until last and penultimate element is compared and swapped.

The algorithm then pops back to the start of the sequence and begins doing the same thing all over again until every value is found to be in the correct position.

#### Performance

In Big O Notation, Insertion Sort's running times are as follows: Best Case: O(n<sup>2</sup>)), Average Case: O(n<sup>2</sup>)), Worst Case: O(n<sup>2</sup>)).

#### Advantages

Bubble Sort is incredibly simple and easy to both understand and implement. It works quite well with small datasets like other comparison sorts such as Selection Sort.

#### Disadvantages

This sort requires several passes over the data, and thus introduces a major factor of inefficiency. Large datasets cripple it and at the end of the day it just doesn't perform well in practice when compared to other comparative sorting algorithms.


### Selection Sort

#### Explanation

The algorithm divides the input array into two parts, a subarray of elements in sorted order, and a subarray of the remaining unsorted elements. The former of the two subarrays begins as an empty array and the latter begins as the entire input array.

The algorithm then sorts an array by repeatedly finding the minimum element from unsorted subarray and moving it into the sorted subarray by swapping it with the leftmost element, i.e it is put in sorted order.

After this the moving the unsorted subarray’s boundary is moved by one element to the right. This increases the sorted subarray and decreases the number of elements left to sort. When the algorithm has finished the unsorted subarray should be empty and the sorted subarray will contain all elements in the input array.

#### Performance

In Big O Notation, Selection Sort's running times are as follows: Best Case: O(n<sup>2</sup>)), Average Case: O(n<sup>2</sup>)), Worst Case: O(n<sup>2</sup>)).

#### Advantages

The advantages of Selection Sort are not unlike the advantages of Insertion sort. The algorithm is stable and in-place, meaning it does not change the relative order of elements with equal keys and only requires a constant amount O(1) of additional memory space. Just like Insertion Sort, Selection Sort performs well when working with small sets of data.

#### Disadvantages

As said earlier, for every element "n" to be sorted, n-squared steps are required, and this leads to great inefficiency for larger sets of data. Insertion Sort is also more efficient than Selection Sort in practice despite the average case running time of both algorithm being equal.


### Insertion Sort

#### Explanation

Insertion sort is based on shifting the elements in the array one by one from an unsorted to a sorted position. For each iteration, the algorithm consumes one input element, the key value, which in turn is added to the segment of the array deemed to be sorted.

The algorithm does its work in-place, iterating along the array, while building the sorted data in it's path. The key value is compared to the largest value in the sorted list, which will always be directly behind it.

If this value behind the key is smaller than the key, it leaves the key value in place and moves to the next key value. If the value behind the key is larger than the key value, it finds the correct position of the key value within the sorted list, shifting all the values larger than the key up to make a space where it is inserted into it's correct position. This is done until no elements remain in front of the sorted data, i.e when the array is completely sorted.

#### Performance

In Big O Notation, Insertion Sort's running times are as follows: Best Case: O(n)), Average Case: O(n<sup>2</sup>)), Worst Case: O(n<sup>2</sup>)).

#### Advantages

The main advantage of the algorithm is it's simplicity, i.e it's very easy to implement. Along with this, Insertion Sort also performs well when working with small sets of data. The algorithm is also stable and in-place, meaning it does not change the relative order of elements with equal keys and only requires a constant amount O(1) of additional memory space. Insertion Sort is also more efficient in practice than most other simple quadratic algorithms such as Selection Sort and Bubble Sort

#### Disadvantages

What holds the algorithm back is that on average, it just doesn't perform as well as other popular sorting algorithms. For every element "n" to be sorted, n-squared steps are required, and this leads to great inefficiency for larger sets of data. Along with this, it's best case running time only applies to already sorted data.


### Quicksort

#### Explanation

Quicksort is based on partitioning of array of data into smaller arrays. The algorithm consists of two functions, quickSort and partition. The The quickSort function picks an element as the pivot and partitions the given array around this value into two smaller arrays, one array containing numbers above that value, the other containing numbers below that value.

The value in question, the pivot value, can be picked in a number of ways. These include: picking the first element as the pivot, picking the last element as the pivot (implemented below in diagram), picking the median as the pivot (implemented below in code), or picking a random element as the pivot.

Quicksort partitions the array based on this chosen pivot value. This partition function is a key part of in Quicksort. Given the array and the chosen pivot, partition puts the pivot value at its correct position in the sorted array. After this the partition function puts all elements less than the pivot before the pivot value, and puts all greater elements after the pivot value.

After this partitioning, the quickSort function calls itself recursively twice to sort the two subarrays which result from the partition. These subarrays have their own pivot values and are passed to the partition function until the value for low is greater than or equal to high, indicating the quickSort function no longer needs to be called.

#### Performance

In Big O Notation, Insertion Sort's running times are as follows: Best Case: O(n log(n)), Average Case: O(n log(n)), Worst Case: O(n<sup>2</sup>)).

#### Advantages

Due to it's elegant recursive design and an efficient average case run time, Quicksort is regarded as quite possibly the best sorting algorithm in practice. Quicksort improves on divide and conquer algorithms like Merge Sort. Unlike Merge Sort, Quicksort is an in-place sorting algorithm which means it require no additional storage. If implemented well, Quicksort can be 2-3 times faster tha Merge Sort and Heap Sort. This is because of the increased simplicity of the inner-most loop operations. Along with this, Quicksort also has the significant advantage in terms of efficiency, faring well when sorting through very large datasets.

#### Disadvantages

Dufficulties with Quicksort include the implementation of the partitioning algorithm and the average efficiency for the worst case scenario, which is not offset by the difficult implementation. Another slight drawback of Quicksort is that at it's worst case running time it's performance is similar to the average case running times of Bubble Sort, Insertion Sort, and Selection Sort. Coupled with this, Quicksort's worst case running time can sometimes be a result of a poorly picked pivot value.
