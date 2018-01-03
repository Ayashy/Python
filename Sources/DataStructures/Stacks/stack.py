
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        print("Pushed " + str(item))
        return self.items.append(item)

    def pop(self):
        print("Popped " + str(self.peek()))
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        display = "----------------\n"
        for item in self.items[::-1]:
            display += str(item) + "\n"
        display += "----------------\n"
        print("\nStack Contents: ")
        return display

    def peek(self):
        return self.items[len(self.items) - 1]

    def sum(self):
        sum = 0
        for item in self.items:
            if item == str(item):
                return "Error: Type String Found"
            sum += item
        return sum

    def pop_all(self):
        while len(self.items) > 0:
            self.items.pop()
        return "The Stack Has Been Cleared"

