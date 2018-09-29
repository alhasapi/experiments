

# (c) 2016 MOKTAR ALHASAPI BAVA
# Third party  implementation of the C-to-BF+C+BF-INTERPRETER


from functools import wraps

INS = ['I', 'D', 'N', 'O', 'F', 'B']
INZ = list("+-,.><")
SIZE_OF_MEMORY = 20

eq_fn = lambda self, other: self.__class__.__name__ == other.__class__.__name__



def build_and_infect():
    classes = dict(zip(INS,
                       map(lambda name: type(name, (object,), {
                           "__str__" : lambda self: name,
                           "__eq__"  : eq_fn
                       }), INS)
                   )
              )
    bg_dict = globals()
    bg_dict.update(classes)
    shw = lambda self: ''.join(map(str,
        self.content[:self.cursor]                     +
        ["<" + str(self.content[self.cursor]) + ">"]   +
        self.content[self.cursor + 1:]
    ))
    bg_dict.update({
        "BfState" : type("BfState", (object,), {
            "cursor"  : 0,
            "content" : map(lambda _: 0, range(SIZE_OF_MEMORY))[:],
            "__str__" : shw
        })
    })
    return bg_dict

def bound_check(func):
    @wraps(func)
    def inner_most_layer(state):
        new_array = map(lambda _: 0, range(SIZE_OF_MEMORY))
        is_out_of_bound = state.cursor + 1 >= len(state.content) or \
                          state.cursor - 1 < 0
        not_start       = not state.cursor == 0
        if is_out_of_bound and not_start:
            # print "--> ", repr(new_array)
            state.content = new_array[:] + state.content[:] + new_array[:]
        func(state)
    return inner_most_layer

def extStruct( expr ):
    token = expr.pop(0)
    if token == '[':
        it = []
        while not expr[0] == ']':
            it.append( extStruct(expr) )
        expr.pop()
        return it
    else: return token

globals().update(build_and_infect())
def parse( chars ): return extStruct( list( chars ) )
@bound_check
def incr( state ):
    state.content[state.cursor] += 1

@bound_check
def decr( state ):
    state.content[state.cursor] -= 1

def fwrd( state ): state.cursor += 1
def bwrd( state ): state.cursor -= 1
def oupt( state ): print(chr(state.content[state.cursor]))
def inpt( state ): state.content[state.cursor] = int(raw_input())

m_dispatch = dict(zip(INZ,
                      [incr, decr, inpt, oupt, fwrd, bwrd]
                  )
             )
def run(instructions):
    initial = BfState()
    state = execute(initial, parse('[' + instructions + ']'))
    print state
    return state

def while_(cond, code):
    while not cond.content[cond.cursor] == 0:
        execute(cond, code)

def execute(state,instructions):
    map(lambda ins:
            while_(state, ins)
            if isinstance(ins, list)
            else m_dispatch[ins](state),
        instructions
    )
    return state

def repl():
    init = BfState()
    while True:
        ins = raw_input("BF> ")
        if ins in ["q", "quit"]: break
        current = execute(init, ins)
        print current
        init = current

if __name__ == '__main__': repl()
