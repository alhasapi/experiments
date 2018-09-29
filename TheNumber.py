
from operator  import add
from itertools import permutations
from functools import partial as curry

THE_SOURCE = '123456789'
FROM_1_TO_9 = (1, 10)

# Adding the case statement to Python.
class case:
    """
    value = 2
    var =
     case(value).
         when(2).execute(atomiq_compositon).
         when(6).execute(atomiq_compositon).
         when(1).execute(fn_c).
         when(4).execute(fn_o).
         when(2).execute(fn_i).
         when(9).execute(fn_u).
        other(lambda a: a).unwrap()
    """
    def __init__( self, value ):
        self.value   = value
        self.out     = None
        self.got_one = False

    def when( self, other ):
        if not self.got_one:
            this = self
            class John:
                def execute( self, fn ):
                   this.out     = fn(this.value)
                   this.got_one = True
                   return this
            if other == self.value: return John()
            return self
        return self
    unwrap  = lambda self: self.out
    execute = lambda self, *args: self
    other   = lambda self,    fn: self if self.got_one else self.__setattr__('out', fn(self.value))

    def other( self, fn ):
        if not self.got_one:
            self.out = fn(self.value)
        return self

def o(*fns):
    atomiq_compositon \
        = lambda f, g: lambda *x: f(g(*x))
    if len(fns) is 2:
        return atomiq_compositon(*fns)
    return reduce(atomiq_compositon, fns)

def track_the_murder():
    to_int  = o(int, curry(reduce, add))
    satisfy = lambda number: all(
                int(str(number)[:n]) % n == 0
                for n in range(*FROM_1_TO_9)
              )
    return to_int(filter(
                o(satisfy, to_int),
                permutations(THE_SOURCE)
              ).pop()
           )
print track_the_murder()
