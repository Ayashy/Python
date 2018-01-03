
def binary_search(lst,size,value):
    low = 0
    high = size -1
    while low <= high:
        middle = (low + high) // 2
        if lst[middle] == value:
            return middle
        elif lst[middle] < value:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def main():

    lst = [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782]
    size = len(lst)
    original_list = ""

    value = int(input("\nInput a value to search for: "))
    print("\nOriginal Array: ")

    for i in lst:
        original_list += str(i) + " "
    print(original_list)
    print("\nBinary Search Big O Notation:\n--> Best Case: O(1)\n--> Average Case: O(log n)\n--> Worst Case: O(log n)\n")

    index = binary_search(lst,size,value)
    if index == -1:
        print(str(value) + " was not found in that array\n")
    else:
        print(str(value) + " was found at index " + str(index))
if __name__ == '__main__':
    main()
