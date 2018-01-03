# Searches


### Explaination

Take an array of entities consisting of two fields: a student name (string) and a grade (integer). An example of this array is:

Array 1:[(Matthew, 3), (John, 9), (Mark, 8),(Luke, 6)]

In this case the data can be searched for based on the string or integer value, with one directly corresponding to the other.

Array 2:[(Matthew, 3), (John, 9), (Mark, 8),(Luke, 6)]

Array 3: [(Matthew, 3), (John, 9), (Mark, 8),(Luke, 6)]

Array 4: [(Matthew, 3), (John, 9), (Mark, 8),(Luke, 6)]

Consider Array 1 above. Each entity has a characteristic values can be searched for to be either a matching string or a matching integer. In Array 2, the entities in bold shows the values returned if searching for all students who achieved a mark over 4. In Array 3 the entities in bold show the value returned when looking for the student with the lowest grade. Similarly in Array 4 the entity in bold shows the value return when looking for the lowest grade rather than the name of the student with the lowest grade. I all cases above, either lexicographically or numerically, the array can be searched thoroughly.

Unfortunately, searching is not always so simple in real world problems. These real world problems often deal with huge datasets consisting of thousands of elements at a time. Searching through these datasets will pull on a fair amount of computing resources. Therefore, the sorting problem is concerned with minimising the amount of resources used when searching through a data structure.

Some properties of good searching algorithms are simplicity, naturalness and efficiency. Essentially, a search algorithm is good when it, is intuitive and easy to understand, requires fewer operations as the distance between the initial and sorted arrays decrease, doesn’t require a large amount of resources.

Each search problem is different, meaning it's important to know what searching algorithm best fits each kind of problem in relation to which is quickest to implement and which works best with a certain type of data(sorted, unsorted). Some searches are better depending on the problem size, with some searches faring worse than other wafting through huge data structures.

The search algorithm you implement, in my opinion, is totally dependant on the problem instance. Different algorithms work better in different situations, so having a knowledge of the different search algorithms in relation to the problem is very important.

### Linear Search (Sequential Search)

#### Explanation

Linear Search, often called Sequential Search, is a search algorithm. It is one of the most fundamental and important of all algorithms. It is simple to understand and implement, yet there are more subtleties to it than most programmers realise.

The input to linear search is a sequence such as an array plus a target value. The output is true if the target item is in the sequence, and false otherwise. If the sequence has n items, then, in the worst case, all n items in the sequence must be checked against the target for equality.

In simple English, the algorithm sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched.

#### Performance

In Big O Notation, Linear Search's running times are as follows: Best Case: O(1)), Average Case: O(n), Worst Case: O(n).

#### Advantages

Linear Search has a little going for it in terms of design. It's simple and easy to remember. Linear Search can work quite efficiently on small data sets and due to how little writing it takes to implement, it can be seen as a more favourable option compared to other algorithms when dealing with such sequences.


#### Disadvantages

In practice, this algorithm is very slow when compared to other search algorithms like Binary Search, and Hashing. Along with this, the algorithm has is less efficient and performs poorly when working with medium - large sized sequences.


### Binary Search

#### Explanation

The first thing of to note about the algorithm is that it can only work on sorted datasets. If the data is not sorted it will not work. The algorithm finds the mid-point of the array and sets the boundaries of low and high(the start and end of the list respectively). The algorithm compares the array at this middle index to the desired value. If it is equal, the algorithm returns the value.

Otherwise, if the value is less or greater than the value at this middle point, the algorithm begins to move the boundaries of low and high. If the desired value is less than the element at the middle index, the low boundary shifts from the old position to the element at the middle index plus one (middle + 1).

If the desired value is greater than the element at the middle index, the high boundary shifts from the old position to the element at the middle index minus one (middle - 1). Each time a boundary moves, the middle is recalculated.

If the desired value is not present in the array, the algorithm returns -1 to signify this.

#### Performance

In Big O Notation, Binary Search's running times are as follows: Best Case: O(1)), Average Case: O(log(n)), Worst Case: O(log(n)).

#### Advantages

Though people get it wrong frequently, the algorithm is fairly simple in design. The big draw with Binary Search is that, in comparison to Linear Search, Binary Search is much faster. Linear search takes, on average N/2 comparisons (where N is the number of elements in the array), and worst case N comparisons. Binary search takes an average and worst-case log2(N) comparisons.

#### Disadvantages

The first thing that holds back Binary Search is the whole sorted data idea. It's fine with static lists, but if they aren't static the data needs to be resorted if elements are continuously added to it. This is not always feasible and can be a drawback of the algorithm, as it requires a non-changing environment. The algorithm is is good with small datasets, but it can be considered overkill for a such small structures.
