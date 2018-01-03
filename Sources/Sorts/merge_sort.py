def merge(lst, low, middle, high):
    left = middle - low + 1
    right = high - middle

    tmpLeft = [0] * (left)
    tmpRight = [0] * (right)

    for i in range(0 , left):
        tmpLeft[i] = lst[low + i]

    for j in range(0 , right):
        tmpRight[j] = lst[middle + 1 + j]

    i = 0
    j = 0
    k = low
    while i < left and j < right:
        if tmpLeft[i] <= tmpRight[j]:
            lst[k] = tmpLeft[i]
            i = i +  1
        else:
            lst[k] = tmpRight[j]
            j = j + 1
        k  = k + 1

    while i < left:
        lst[k] = tmpLeft[i]
        i = i + 1
        k = k + 1

    while j < right:
        lst[k] = tmpRight[j]
        j = j + 1
        k = k + 1


def merge_sort(lst,low,high):
    if low < high:
        middle = (low + (high-1)) // 2
        merge_sort(lst, low, middle)
        merge_sort(lst, middle+1, high)
        merge(lst, low, middle, high)
    else:
        pass


def main():

    lst = [10, 7, 3, 9, 18, -4, 67, 32, 0, 21]
    high = len(lst) - 1
    low = 0
    print("\nOriginal Array: ")
    print(lst)

    print("\nSorted Array: ")
    merge_sort(lst,low,high)
    print(lst)

    print("\nMerge Sort Big O Notation:\n--> Best Case: O(n log n)\n--> Average Case: O(n log n)\n--> Worst Case: O(n log n)\n")

if __name__ == '__main__':
    main()
