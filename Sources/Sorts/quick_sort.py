def partition(lst, low, high):
   pivot = lst[low]

   while (low <= high):
      while lst[low] < pivot:
         low = low + 1

      while lst[high] > pivot:
         high = high - 1

      if low <= high:
         tmp = lst[low]
         lst[low] = lst[high]
         lst[high] = tmp

         low = low + 1
         high = high - 1

   return low


def quick_sort(lst, low, high):
   if high <= low:
      return

   partition_index = partition(lst, low, high)
   if low < partition_index - 1:
      quick_sort(lst, low, partition_index - 1)
   if high > partition_index:
      quick_sort(lst, partition_index, high)

def main():
   lst = [10, 7, 3, 9, 18, -4, 67, 32, 0, 21]
   high = len(lst) - 1
   low = 0

   print("\nOriginal Array: ")
   print(lst)

   print("\nSorted Array: ")
   quick_sort(lst,low,high)
   print(lst)

   print("\nQuicksort Big O Notation:\n--> Best Case: O(n log n) \n--> Average Case: O(n log n)\n--> Worst Case: O(n^2)\n")
if __name__ == '__main__':
    main()
