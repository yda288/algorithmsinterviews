
from collections import defaultdict
from collections.abc import Sequence
from .constants import CONST_KNIGHT_STRIDES
from itertools import chain, product

class BoundedIndexSeq(Sequence):
    """This is just a list which does not permit negative indexing or slicing.
    Defensive so as to prevent wraparound indexing by consumers.    
    """

    def __init__(self, seq):
        self._seq = seq 

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                raise IndexError("Negative indices disabled. Sequence does not wraparound.")
        if isinstance(key, slice):
            if key.start < 0 or key.stop < 0:
                raise IndexError("Negative slicing disabled.")
            
        return self._seq.__getitem__(key)
        
    def __len__(self):
        return len(self._seq)
 
       
class Keypad(object):
    """Keypad representation delegating to the BoundedSeq constraint"""
    def __init__(self, keypad):
        self._keypad = BoundedIndexSeq(tuple([
            BoundedIndexSeq(tuple(keypad_line)) for keypad_line in keypad
            ]))
            
    def __getitem__(self, key):
        return self._keypad.__getitem__(key)
        
    @property
    def height(self):
        return len(self._keypad)
        
    @property
    def width(self):
        return len(self._keypad[0])
        
    @property
    def rows(self):
        return self.height
        
    @property
    def columns(self):
        return self.width
        
    def flatten(self):
        """Flattened single row keypad representation"""
        self.flat_keypad=list(filter(lambda x: x != ' ', chain(*self._keypad)))
        return self.flat_keypad
        
    def key_to_idx(self):
        """Map ordered keypad keys to indices"""
        return {val:idx for idx,val in enumerate(self.flat_keypad)}


class Adjacency(object):
    """Adjacency graph builder"""
    def __init__(self, keypad):
        self._adjacency = defaultdict(set)
        self.keypad = keypad
        
    def build_adjacency(self):
        
        for row_ix, col_ix in product(
		range(self.keypad.height), 
		range(self.keypad.width)
		):
            if ' ' not in str(self.keypad[row_ix][col_ix]): ##only permit alphanumeric sources ie exclude special characters
                for _ in CONST_KNIGHT_STRIDES:
                    dest_row_ix = row_ix + _[0] ##TRIM the strides on the boundaries. MASK STRIDES should exist inside keypad
                    dest_col_ix = col_ix + _[1]
                    if (
                    dest_row_ix >= 0 and dest_row_ix < self.keypad.height and  ##discard negative and list indices out of range
                    dest_col_ix >= 0 and dest_col_ix < self.keypad.width
                    ):
                        self._append_adjacency(row_ix, col_ix, row_ix + _[0], col_ix + _[1])
                    
        return defaultdict(tuple, ((k, tuple(v)) for k, v in self._adjacency.items()))
    
    """ For a given keypad digit at (row_ix, col_ix) this method
    appends permissible destination digits at (dest_row_ix, dest_col_ix) to adjacency """
    def _append_adjacency(self, row_ix, col_ix, dest_row_ix, dest_col_ix):
             
            dest = self.keypad[dest_row_ix][dest_col_ix] 
            
            if ' ' not in str(dest): ##only permit alphanumeric destinations
                self._adjacency[
                self.keypad[row_ix][col_ix]
                ].add(
                    dest           
                )
    
    
        