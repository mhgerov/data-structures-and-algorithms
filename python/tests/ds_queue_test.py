import unittest
from dsa.ds_queue import Queue

class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        result = queue.pop()
        self.assertEqual(result,1)