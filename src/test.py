import unittest
from check import check_Restock

class TestCases(unittest.TestCase):
    def test_example(self):
        arr = [1, 0, 2, 3, 0, 4, 5]
        check_Restock(arr)
        self.assertEqual(arr, [1, 0, 0, 2, 3, 0, 0])
 
    def test_no_zeros(self):
        arr = [1, 2, 3, 4, 5]
        check_Restock(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
 
    def test_all_zeros(self):
        # [0,0,0] -> each 0 duplicates but list stays length 3: [0,0,0]
        arr = [0, 0, 0]
        check_Restock(arr)
        self.assertEqual(arr, [0, 0, 0])
 
    def test_single_zero(self):
        # Only one slot; the duplicate has nowhere to go, list stays [0]
        arr = [0]
        check_Restock(arr)
        self.assertEqual(arr, [0])
 
    def test_single_non_zero(self):
        arr = [7]
        check_Restock(arr)
        self.assertEqual(arr, [7])
 
    def test_zero_at_start(self):
        arr = [0, 1, 2, 3]
        check_Restock(arr)
        self.assertEqual(arr, [0, 0, 1, 2])
 
    def test_zero_at_end(self):
        # The trailing 0 fills its own slot; no room for the duplicate
        arr = [1, 2, 3, 0]
        check_Restock(arr)
        self.assertEqual(arr, [1, 2, 3, 0])
 
    def test_empty_list(self):
        arr = []
        check_Restock(arr)
        self.assertEqual(arr, [])
 
    def test_zero_near_end(self):
        arr = [1, 2, 0, 3]
        check_Restock(arr)
        self.assertEqual(arr, [1, 2, 0, 0])


if __name__ == '__main__':
    unittest.main()