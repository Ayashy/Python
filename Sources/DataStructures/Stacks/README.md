# Stacks


### Explanation

A stack is a collection, meaning that it is a data structure that contains multiple elements.

A stack is sometimes called a “Last in, First out” or LIFO data structure, because the last item added is the first to be removed. Think of it as a pile of books, with each book being an item on the stack. You can only take the top book off the pile if you want to preserve it.

### Implementing Stacks With Python

The list operations that Python provides are not unlike the operations which define a stack. We can write code to translate from the stack to the built-in operations. Some key operations are detailed below.

#### Key Operations

A `Stack` object has an attribute named `items` that is a list of items which acts as the stack. The `__init__` method sets items to an empty list.

To add a new item to the stack, the `push` method appends said item onto items. To take the top item off the stack, the `pop` method uses the list pop method to remove the top item.

If you want to check if the stack is empty, the `is_empty` method simply compares the list items to the empty list.

#### Other Operations
Aside from the aforementioned operations, I've added some more method which allow you to play around with the structure.

The `size` method returns the size of the stack (len(list)).

The `display` method prints out the formatted contents of the stack.

The `peek` method shows the final element of the queue which is the next to be dequeued.

The `clear` method clears the queue so it is empty (len(list) == 0).
