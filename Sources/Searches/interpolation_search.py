def interpolation_search(lst, low, high, value):
    while low <= high and value >= lst[low] and value <= lst[high]:
        pos  = low + int(((float(high - low) / (lst[high] - lst[low])) * (value - lst[low])))
        if lst[pos] == value:
            return pos
        if lst[pos] < value:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def main():

    lst = [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782]
    low = 0
    high = len(lst) - 1
    original_list = ""

    value = int(input("\nInput a value to search for: "))
    print("\nOriginal Array: ")

    for i in lst:
        original_list += str(i) + " "
    print(original_list)
    print("\nInterpolation Search Big O Notation:\n--> Best Case: O(1)\n--> Average Case: O(log(log(n)))\n--> Worst Case: O(n)\n")

    index = interpolation_search(lst, low, high, value)
    if index == -1:
        print(str(value) + " was not found in that array\n")
    else:
        print(str(value) + " was found at index " + str(index))
if __name__ == '__main__':
    main()
