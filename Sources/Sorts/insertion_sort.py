def insertion_sort(lst,size):
  for i in range(1,size):
    pos = lst[i]
    j = i - 1
    while (j > -1) and pos < lst[j]:
      lst[j + 1] = lst[j]
      j = j - 1
    lst[j + 1] = pos


def main():

    lst = [10, 7, 3, 9, 18, -4, 67, 32, 0, 21]
    size = len(lst)

    print("\nOriginal Array: ")
    print(lst)

    print("\nSorted Array: ")
    insertion_sort(lst,size)
    print(lst)

    print("\nInsertion Sort Big O Notation:\n--> Best Case: O(n)\n--> Average Case: O(n^2)\n--> Worst Case: O(n^2)\n")

if __name__ == '__main__':
    main()
