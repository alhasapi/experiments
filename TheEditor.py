
from pprint    import pprint  as p
from functools import partial as curry

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = self.prev = None
        self.down  = self.up   = None

    @classmethod
    def new(cls, *args):
        return cls(*args)

class NodeManager:
    def __init__(self, limit=100):
        self.partial_line = []
        self.limit = limit
        self.lines = []

    def head(self):
        return self.lines[0][0] if self.lines else None

    def insert(self, value):
        node = Node.new( value )

        # Local helper function to transpose a list of lists
        def transpose( lst ):
            fn = lambda i: map(lambda arr: arr[i], lst)
            return map(fn, range(self.limit))

        # Helper function for connecting two adjacent nodes horizontaly
        def _bridge(n1, n2):
            n1.next, n2.prev = n2, n1
            return n2

        # Helper function for connecting two adjacent nodes verticaly
        def __bridge(n1, n2):
            n1.down, n2.up  = n2, n1
            return n2

        # When the line limit is reached
        if len(self.partial_line) == self.limit:
            the_line = self.partial_line[:]
            reduce(_bridge, the_line) # connect horizontaly each node to his nearbord
            # Save the line
            # TODO: The head of the line is the only thing we need here to access to the whole line.
            #       Storing the complete line is irrelevant.
            #       Find a way to write it whithout that evident messyness.
            self.lines.append( the_line )
            if len( self.lines ) >= 2:
                map( curry( reduce,__bridge ), transpose(self.lines))
            self.partial_line = []
        self.partial_line.append( node )

    def __walker(self, start, node, *fns):
    	return self.__walker(
		   fns[0](start, node), 
		   fns[1](node), 
		   fns
		) if node else start

    line, whole = map(curry(self.__walker, "", node), 
                      [ [lambda s, n: s + n.value,    lambda n: n.next],
						[lambda s, n: s + self.line,  lambda n: n.down]
					  ])
					  
    def _iter_lines( self ):
        line = self.head()
        while line:
            yield line
            line = line.down

    def __iter__(self):
        for line in self._iter_lines():
            node = line
            while node:
                yield node.value
                node = node.next

    def show(self):
        head  = self.head()
        if not head: return ""
        return self.whole(head)
        
    @classmethod
    def new_manager(cls, *arg):
        return cls(*arg)

    def write_to_file(self, fname):
        with open(fname, "a") as outSide:
            outSide.write(self.show())

    @classmethod
    def From_file(cls, fname):
        manager = cls.new_manager()
        with open(fname, "r") as outSide:
            map(manager.insert, outSide.read())
        return manager

    def __str__(self):
        return self.show()
    __repr__ = __str__

q = NodeManager.From_file("configuration.org.txt")
print q.show()
