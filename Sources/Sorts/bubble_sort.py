def bubble_sort(lst,size):
  for i in range(size):
    for j in range(size - i - 1):
      if lst[j] > lst[j + 1]:
        tmp = lst[j]
        lst[j] = lst[j + 1]
        lst[j + 1] = tmp

def main():
    lst = [10, 7, 3, 9, 18, -4, 67, 32, 0, 21]
    size = len(lst)

    print("\nOriginal Array: ")
    print(lst)

    print("\nSorted Array: ")
    bubble_sort(lst,size)
    print(lst)

    print("\nBubble Sort Big O Notation:\n--> Best Case: O(n)\n--> Average Case: O(n^2)\n--> Worst Case: O(n^2)\n")

if __name__ == '__main__':
    main()
