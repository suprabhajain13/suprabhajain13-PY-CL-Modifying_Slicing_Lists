import unittest
from src.main.lab import create_list, modify_list, slice_list

class TestLabFunctions(unittest.TestCase):
    def test_create_list_positive(self):
        # Test for a positive number of elements
        self.assertEqual(create_list(5), [1, 2, 3, 4, 5])

    def test_create_list_zero(self):
        # Test for zero elements
        with self.assertRaises(ValueError) as context:
            create_list(0)
        self.assertEqual(str(context.exception), "Number of elements must be positive")

    def test_create_list_negative(self):
        # Test for a negative number of elements
        with self.assertRaises(ValueError) as context:
            create_list(-5)
        self.assertEqual(str(context.exception), "Number of elements must be positive")

    def test_modify_list(self):
        # Test case for modifying the list
        my_list = [1, 2, 3, 4, 5]
        modify_list(my_list, value_to_append=6, value_to_insert=0, value_to_remove=3)
        self.assertEqual(my_list, [0, 1, 2, 4, 5, 6])

    def test_slice_list(self):
        # Test case for slicing the list with default parameters
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(slice_list(my_list), [1, 2, 3])

        # Test case for slicing the list with custom parameters
        self.assertEqual(slice_list(my_list, start=1, end=4), [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
