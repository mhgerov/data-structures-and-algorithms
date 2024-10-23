import unittest
import dsa.algos_search_binary as asb

class TestBinarySearch(unittest.TestCase):

    def test1(self):
        arr = [2,4,6,8,10,12]
        value = 4
        result = asb.binary_search(arr,value)
        self.assertEqual(result,1)
        
    def test_notfound(self):
        arr = [2,3,6,8,10,12]
        value = 4
        result = asb.binary_search(arr,value)
        self.assertEqual(result,-1)
        
