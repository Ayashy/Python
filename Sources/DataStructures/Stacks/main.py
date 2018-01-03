from stack import Stack


def main():
    stack = Stack()

    stack.push(3)
    stack.push(7)
    stack.push(18)

    print(stack.display())

    stack.pop()
    print(stack.display())
    stack.pop_all()
    
    lst = [1, 8, 10, -7, 34]
    
    print(stack.sum())
    stack.pop_all()
    
if __name__ == '__main__':
    main()
