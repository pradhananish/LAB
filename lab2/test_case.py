import unittest
from merge import merge_sort
from quick import quick_sort

class SortTestCase(unittest.TestCase):
    def test_merge_sort(self):
        A = [2, 3, 1, 5, 6, 4]
        sortList = [1, 2, 3, 4, 5, 6]
        merge_sort(A, 0, len(A) - 1)
        self.assertListEqual(A, sortList)
        
    def test_quick_sort(self):
        A = [10, 7, 8, 9, 1, 5]
        B = [3, 2, 1]
        C = [5, 10, 15, 20, 25]
        
        sortList_A = [1, 5, 7, 8, 9, 10]
        sortList_B = [1, 2, 3]
        sortList_C = [5, 10, 15, 20, 25]
        
        quick_sort(A, 0, len(A) - 1)
        quick_sort(B, 0, len(B) - 1)
        quick_sort(C, 0, len(C) - 1)
        
        self.assertListEqual(A, sortList_A)
        self.assertListEqual(B, sortList_B)
        self.assertListEqual(C, sortList_C)
        
if __name__ == '__main__':
    unittest.main()
