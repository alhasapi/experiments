
def mkLine(ini, between):
    return " "*ini + "/" + " "*between + "\\"

def odds():
    n = 1
    while 1:
            if n % 2: yield n
            n += 1

def get_rep_node(val, n):
    yield " " * (n + 1) + str( val ) + "\n"
    for i, v in zip(range(n, 1, -1), odds()):
        yield mkLine(i, v) + "\n"

def enlarge(rep_node):
    pass

def show_node(n, v=10):
    print ''.join(get_rep_node(n, v))
