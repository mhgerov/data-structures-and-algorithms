import unittest
import dsa.algos_sort_selection as ass

class TestSelectionSort(unittest.TestCase):

    def test1(self):
        arr = [1,7,3,2,5]
        result = ass.selection_sort(arr)
        self.assertEqual(result,[1,2,3,5,7])