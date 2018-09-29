
def col(idx, ps, string, limit=3):
    if idx - ps >= limit: return (idx, "")
    idh, st = col(idx + 1, ps, string)
    return (idh, string[idx] + st)

def extract_group(idx, string):
    return col(idx, idx, string)

dc = { "abc" :  2,
       "def" :  3,
       "ghi" :  4,
       "jkl" :  5,
       "mno" :  6,
       "pqrs":  7,
       "tuv" :  8,
       "wxyz" : 9 }

cd = dict((v, k) for (k, v) in dc.items())
def encypher(string):
    chunks = string.split()
    g_key  = lambda z: [key for key in dc.keys() if z in key][0]
    fn     = lambda z: str(dc[g_key(z)]) * (g_key(z).index(z) + 1)
    return '0'.join(''.join(map(fn, u)) for u in chunks)

def ex(idx, string):
    v, s = "", string[idx]
    while idx < len(string) and s == string[idx]:
        v, idx = v + s, idx + 1
    return (idx, v)

def extr(String):
    idx, v  = ex(0, String)
    content = [v]
    while idx < len(String):
        idx, v = ex(idx, String)
        content.append(v)
    return content

def decypher(string):
    # TODO: The redundancy analyser isn't yet implemented,
    chunks = string.split('0')
    fn = lambda u: cd[int(u[0])][len(u) - 1]
    p1 = map(extr, chunks)
    return [''.join(map(fn, u)) for u in p1 ]

def redundancy_analyser(items):
    pass
