class Array:
    def __init__( self, size ):
        self.size = size
        self.content = []
        for i in range(size):
            self.content.append(None)
    
    def __setitem__( self, idx, value ):
        self.content[idx] = value
    
    def __getitem__( self, idx ):
        return self.content[idx]

    def __len__( self ):
        return self.size        


class MaxHeap :
    def __init__( self, maxSize ):
        self._elements = Array( maxSize )
        self._count = 0

    def __len__( self ):
        return self._count

    def capacity( self ):
        return len( self._elements )

    def add( self, value ):
        assert self._count < self.capacity(), "Cannot add to a full heap."
 
        self._elements[ self._count ] = value
        self._count += 1
        # Sift the new value up the tree.
        self._siftUp( self._count - 1 )
        
    def extract( self ):
        assert self._count > 0, "Cannot extract from an empty heap."        
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[ self._count ]       
        self._siftDown( 0 )
        return value
        
    def _siftUp( self, ndx ):
        if ndx > 0 :
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent] :
                tmp = self._elements[ndx]
                self._elements[ndx] = self._elements[parent]
                self._elements[parent] = tmp
                self._siftUp( parent )

    def _siftDown( self, ndx ):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # Determine which node contains the larger value.
        largest = ndx
        if left < self._count and self._elements[left] >= self._elements[largest] :
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx :
            tmp = self._elements[ndx]
            self._elements[ndx] = self._elements[largest]
            self._elements[largest] = tmp
            self._siftDown( largest )        

def hp( theSeq ):
    n = len(theSeq)
    heap = MaxHeap( n )
    
    for item in theSeq :
        heap.add( item )
    lst = []
    for i in range( n, 0, -1 ) :
        lst.append(heap.extract())
    return list(reversed(lst)), heap

from random import randint as r
from functools import partial as p
rd = p(r, 1, 100)

def lst(): return [rd() for i in range(10)]
l = lst()


