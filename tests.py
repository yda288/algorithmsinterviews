import unittest
from collections import defaultdict
from src.knightssequences import Keypad, Adjacency, BoundedIndexSeq

""" Unit tests for the requested case. """
class TestKeyapd(unittest.TestCase):
    
    def setUp(self):
        """
         Setup testsuite.
         """
        bounded_seq = ['A','B','C','D','E']
        
        keypad = [
            ['A','B','C','D','E'],
            ['F','G','H','I','J'],
            ['K','L','M','N','O'],
            [' ', 1,  2,  3, ' ']
            ]
            
        self.bounded_seq = BoundedIndexSeq(bounded_seq)
        self.keypad = Keypad(keypad)
        self.adjacency = Adjacency(self.keypad).build_adjacency()
        
            
    def test_negative_index_error(self):
        
        with self.assertRaisesRegex(IndexError, 'Negative indices disabled. Sequence does not wraparound.'):
            self.bounded_seq[-1]

    def test_negative_substr_slice_error(self):
        
        with self.assertRaisesRegex(IndexError, 'Negative slicing disabled.'):
            self.keypad[-1:][0]
    
    
    
if __name__ == '__main__':
    unittest.main()
    