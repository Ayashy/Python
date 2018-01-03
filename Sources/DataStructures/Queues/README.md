# Queues


### Explanation

A queue is a collection, i.e, it is a data structure that has many elements.

A queue is easy to find analgoy for, just think of a line of people waiting for something, be it to use an ATM or pay for goods in a supermarket. In most cases, the first person in line is the next one to be served. This queueing policy is called “First in, First out”, making the queue detailed in this repo a FIFO data structure.

### Implementing Queues With Python

 List operations defined in Python are similar to the operations that define a queue. We can translate queue operations to built in Python operations easily, here are some key queue operations.

#### Key Operations

A `Queue` object has an attribute named `items` (list of items acting as the queue). The `__init__` method sets items as an empty list.

To add a new item to the queue, the `enqueue` method inserts the item to the zeroth position of the list. To remove the item and the end of the queue, the `dequeue` method uses the list pop method to take off the last item in the list.

To check if the queue is empty, the `is_empty` method simply compares the list items to the empty list.

#### Other Operations
Aside from the aforementioned operations, I've added some more method which allow you to play around with the structure.

The `size` method returns the size of the queue (len(list)).

The `display` method prints out the formatted contents of the queue.

The `peek` method shows the current top element of the stack.

The `sum` method find the total sum of the contents of the stack (if all elements are not of type string).

The `pop_all` method clears the stack until it is empty (len(list) == 0).
