import unittest
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from count_sort import counting_sort
from merge_sort import merge_sort


class TestSort(unittest.TestCase):

    def test_bubble(self):
        unsorted = [5, 4, 3, 2, 1]
        sorted_lst = [1, 2, 3, 4, 5]
        length = len(unsorted)
        bubble_sort(unsorted, length)
        self.assertEqual(sorted_lst, unsorted)

    def test_selection(self):
        unsorted = [5, 4, 3, 2, 1]
        sorted_lst = [1, 2, 3, 4, 5]
        length = len(unsorted)
        selection_sort(unsorted, length)
        self.assertEqual(sorted_lst, unsorted)

    def test_quick(self):
        unsorted = [1, 2, 3, 4, 5]
        sorted_lst = [1, 2, 3, 4, 5]
        high = len(unsorted) - 1
        low = 0
        quick_sort(unsorted, low, high)
        self.assertEqual(sorted_lst, unsorted)

    def test_insertion(self):
        unsorted = [5, 4, 3, 2, 1]
        sorted_lst = [1, 2, 3, 4, 5]
        length = len(unsorted)
        insertion_sort(unsorted, length)
        self.assertEqual(sorted_lst, unsorted)

    def test_count(self):
        unsorted = [5, 4, 3, 2, 1]
        sorted_lst = [1, 2, 3, 4, 5]
        result = counting_sort(unsorted)
        self.assertEqual(sorted_lst, result)

    def test_merge(self):
        unsorted = [5, 4, 3, 2, 1]
        sorted_lst = [1, 2, 3, 4, 5]
        high = len(unsorted) - 1
        low = 0
        merge_sort(unsorted, low, high)
        self.assertEqual(sorted_lst, unsorted)
if __name__ == '__main__':
    unittest.main()

