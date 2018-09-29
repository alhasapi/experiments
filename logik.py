"""
TODO: a deep refactoring is needed
It takes a logical expression and build its logical table.
"""

import operator
import functools as fn
import random as rd
import sys

LOGO = '\n'.join([
"$$\                          $$\ $$\       ",
"$$ |                         \__|$$ |      ",
"$$ |      $$$$$$\   $$$$$$\  $$\ $$ |  $$\ ",
"$$ |     $$  __$$\ $$  __$$\ $$ |$$ | $$  |",
"$$ |     $$ /  $$ |$$ /  $$ |$$ |$$$$$$  / ",
"$$ |     $$ |  $$ |$$ |  $$ |$$ |$$  _$$<  ",
"$$$$$$$$\\$$$$$$  |\$$$$$$$ |$$ |$$ | \$$\ ",
"\________|\______/  \____$$ |\__|\__|  \__|",
"                   $$\   $$ |              ",
"                   \$$$$$$  |              ",
"                    \______/   Logik interpreter (c) qmilocevic 2014 MIT "
])

OPS = {
    "not": operator.not_,
    "and": operator.and_,
    "or":  operator.or_,
    "imp": lambda a, b: (not a) or b,
    "eq": lambda a, b: OPS["imp"](a, b) and OPS["imp"](b, a)
}
def cop(logical_op, *lst):
    """
    Apply a logical operator on list of binary values.
    """
    return map(lambda x: OPS[logical_op](*x), zip(*lst))

def rd_tables(size):
    """
    Generate a random list of binary values
    """
    return [rd.randint(0, 1) for _ in range(size)]

ALL = {key : fn.partial(cop, key) for key in OPS}

TEMPLATE = lambda obj: [
    "---------",
    "         ",
    "    " + str(obj) + "    ",
    "         ",
    "         "
]

COLUMN = [
    "+", "|", "|", "|",
]

def is_an_sexpr(code):
    return '(' in code and ')' in code

def join(one, two):
    """
    Join two objects owning the same inner representation.
    """
    return list(map(lambda z: operator.add(*z), zip(one, two)))

def append(obj, other):
    """
    Append two objects.
    """
    return join(join(obj, COLUMN), other)

def wrap(obj):
    """
    Add a column before and after :obj
    """
    return join(join(COLUMN, obj), COLUMN)

def lex_it(expr):
    """
    Inserting spaces between backets and split expr accoring to them
    """
    normalizer = lambda u: f" {u} " if u in "()" else u
    return "".join(map(normalizer, expr)).split()

def extract_structure(expr):
    """
        The lisp-like structure of logik's code
        makes parsing utterly straightforward.
    """
    if not expr:
        raise SyntaxError("Accidental End-Of-File!")
    token = expr.pop(0)
    if token == '(':
        tree = []
        while not expr[0] == ')':
            tree.append(extract_structure(expr))
        expr.pop(0)
        return tree
    return token

def parse(source_code):
    """
    Returns a tree representation of source_code
    """
    return extract_structure(
        lex_it(source_code)
    )


def generate_table(size):
    """
    Generate the logical table according to size
    """

    def bin_(value):
        """convert :value to binary """
        return bin(value)[2:]

    def map_(func, items):
        """ A strict map """
        return list(map(func, items))

    def padd_me(size, bin_rep):
        """ Padd a binary representation of number with zeros according to :size"""
        return "0"*(size - len(bin_rep)) + bin_rep

    binaries = map(bin_, range(2**size))
    normalize = lambda items: [int(i) for i in items]
    return map_(normalize, map_(fn.partial(padd_me, size), binaries))

def transpose(table):
    """
    Applying the mathematical operation named transposition on :table
    """
    return [[q[i] for q in table] for i in range(len(table[0]))]


def flatten(lst):
    """
    Convert an arbitrarily nested list to a single level list, a flat list in a nutshell.
    """
    if not lst:
        return lst
    if not isinstance(lst[0], list):
        return [lst[0]] + flatten(lst[1:])
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])

def vars_info(expr):
    """
    How many variables in the expression?
    """
    def get_variables(expr):
        """
        returns the list of variables in expr
        """
        return list(set(filter(lambda item: len(item) == 1, flatten(expr))))
    variables = get_variables(expr)
    return len(variables), variables

def load_env_from_code(expr):
    """
    returns a dictionary witch maps each variables to its table.
    """
    variables_number, variables = vars_info(expr)
    tables = transpose(generate_table(variables_number))
    return dict(zip(variables, tables))

def evaluate(expr, env):
    """
    Execute any logical expr and return its output.
    """
    if expr[0] == 'not':
        _, operand = expr
        return ALL["not"](evaluate(operand, env))
    if expr[0] in ALL.keys():
        l_op, operand_1, operand_2 = expr
        return ALL[l_op](evaluate(operand_1, env), evaluate(operand_2, env))
    return env[expr]

def run(expr):
    """
    The entry point, our main to execute logical expressions
    """
    env = load_env_from_code(expr)
    return [int(s) for s in evaluate(expr, env)], env

def vertical(lst):
    return wrap(fn.reduce(append, list(map(TEMPLATE, lst))))
def horizontal(lst):
    return fn.reduce(operator.add, lst) + [lst[0][0]]

def show(items):
    return '\n'.join(items)

def wrap2(items):
    return items + [items[0]]

def single(items):
    return show(wrap2(vertical(items)))

def pretty_print(out, env):
    """
    self.__name__, in a nutshell
    """
    waiting_to_be_rendered = list(map(vertical, transpose(list(env.values()) + [out])))
    print(show(horizontal(waiting_to_be_rendered)))

ENV = None

def repl():
    """
    The Read Eval Print Loop
    """
    global ENV
    while True:
        try:
            code = input("~> ")
            if not code:
                continue
            if code in ["q", "quit"]:
                raise EOFError
            expr = parse(code)
            if ENV and code in ENV:
                print(single(ENV[code]))
                continue

            ENV = load_env_from_code(expr)
            pretty_print(*run(expr))

        except KeyboardInterrupt:
            sys.stdout.flush()
            continue

        except EOFError:
            print("Good bye :-)")
            break

if __name__ == '__main__':
    print(LOGO)
    repl()
