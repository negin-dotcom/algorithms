import unittest

from my_algorithms.merge_sort_implementation import merge_sort


class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.one_element_array = [10]
        self.two_element_array = [10, 5]
        self.array = [0, 8, 1, 6, 400, 52, 1, 3, 7, 1, 5]

    def test_merge_sort_with_one_element(self):
        self.assertEqual(
            merge_sort(self.one_element_array),
            [10]
        )

    def test_merge_sort_with_two_elements(self):
        self.assertEqual(
            merge_sort(self.two_element_array),
            [5, 10]
        )

    def test_merge_sort_for_large_array(self):
        self.assertEqual(
            merge_sort(self.array),
            [0, 1, 1, 1, 3, 5, 6, 7, 8, 52, 400]
        )


if __name__ == "__main__":
    unittest.main()