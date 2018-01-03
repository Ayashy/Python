

def selection_sort(lst,size):
  for i in range(size):
    pos = i
    for j in range(i + 1 ,size):
      if lst[j] < lst[pos]:
        pos = j

    tmp = lst[pos]
    lst[pos] = lst[i]
    lst[i] = tmp



def main():

    lst = [10, 7, 3, 9, 18, -4, 67, 32, 0, 21]
    size = len(lst)

    print("\nOriginal Array: ")
    print(lst)

    print("\nSorted Array: ")
    selection_sort(lst,size)
    print(lst)

    print("\nSelection Sort Big O Notation:\n--> Best Case: O(n^2)\n--> Average Case: O(n^2)\n--> Worst Case: O(n^2)\n")

if __name__ == '__main__':
    main()
