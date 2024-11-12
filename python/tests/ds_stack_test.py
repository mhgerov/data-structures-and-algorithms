import unittest
from dsa.ds_stack import Stack

class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(7)
        stack.push(7)
        result = stack.pop()
        self.assertEqual(result,7)