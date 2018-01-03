from queue import Queue


def main():
    queue = Queue()

    queue.enqueue('hello')
    queue.enqueue('dog')
    queue.enqueue(3)

    print(queue.display())
    queue.dequeue()

    print(queue.display())
    queue.dequeue()

    print(queue.display())
    queue.dequeue()

    print(queue.display())
    queue.dequeue()

    queue.enqueue('world')
    queue.enqueue('cat')
    queue.enqueue(1)
  
    print(queue.size())
    
    print(queue.display())
    queue.clear()

    print(queue.display())
 

if __name__ == '__main__':
    main()
