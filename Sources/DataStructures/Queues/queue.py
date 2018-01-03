class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if len(self.items) <= 0:
            print("The Queue Is Empty")
            return
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        display = "----------------\n"
        for item in self.items:
            display += str(item) + " "
        display += "\n----------------\n"
        print("\nQueue Contents: ")
        return display

    def peek(self):
        return self.items[len(self.items) - 1]

    def clear(self):
        while len(self.items) > 0:
            self.items.pop()
        print("The Queue Has Been Cleared")
        return
