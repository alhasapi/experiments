
class Node:
    def __init__(self, cs, n):
        self.cs = cs
        self.next = n

a = Node(1, Node(2, Node(3, Node(4, None))))
b = Node(5, Node(6, Node(7, Node(8, None))))
b.next.next.next.next = b
a.next.next.next.next = b

def next(node): return node.next

def loopSize(start):
    dc, node, s = {}, start, 0
    while not dc.has_key(node.cs):
        s, dc[node.cs], node = (s + 1, True, node.next)
    while node.cs != start.cs: s, start = (s - 1, start.next)
    return s

def cmt(start_node, node, s):
    if start_node.cs != node.cs:
        return cmt(next(start_node), node, s - 1)
    return s

def lpSize(sn, start, dc, s):
    if not dc.has_key(start.cs):
        return lpSize(sn, next(start),
                      dict(dc.items() + [(start.cs,True)]), s + 1)
    return cmt(sn, start, s)

def pSize(start):
    return lpSize(start, start, {}, 0)

def conseqsOf(x, items):
    for (idx, v) in enumerate(items):
        if x == v:
            s = []
            f = idx
            while f < len(items) and items[f] == x:
                s.append(x)
                f += 1
            return (s, f)
    return ([], 0)

