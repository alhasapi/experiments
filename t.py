
class S(list):
    def __init__(self, *args):
        for i in [map, filter, sum]:
            fn = lambda *a: i(*(a + (self,)))
            setattr(self, i.__name__, fn)
        super(S, self).__init__(*args)

def calcul(path, sep):
    data   = open(path).read().split(sep)
    data_1 = map(lambda u: u.splitlines(), data)
    data_2 = map(lambda u: filter(lambda k: k!= '', u), data_1)
    data_3 = map(lambda u: map(int, u), data_2)
    sommes = list(map(sum, data_3))
    return sommes, sum(sommes)

def cl(path, seq):
    sommes =                                         \
    S(open(path).read().split(sep))                  \
      .map(lambda u: u.splitlines())                 \
      .map(lambda u: filter(lambda k: k is not '', u))\
      .map(lambda u: map(int, u))
    return [sommes, sum(sommes)]
      

if __name__ == '__main__':
    import sys
    size = len(sys.argv)
    if size != 3:
        print("Usage: %s fichier separateur" %(sys.argv[0]))
    else:
        fname, sep = sys.argv[1:]
        items, sm = calcul(fname, sep)
        print("Les differentes sommes: " + repr(items))
        print("La somme totale est: " + str(sm))
