import argparse
import sys
import yaml
from pprint import pprint as PP


parser = argparse.ArgumentParser()
parser.add_argument("--far", nargs=3, metavar=('PREFIX','PATH','REPLACEMENT'), help="Find and replace in list by prefix.")
parser.add_argument("--dfl", nargs=3, metavar=('PREFIX','PATH','REPLACEMENT'), help="Drop from list by prefix.")
parser.add_argument("--set", nargs=2, metavar=('PATH','VALUE'))
parser.add_argument("--unset", nargs=1, metavar=('PATH'))
parser.add_argument("--addnull", nargs=1, metavar=('PATH'))
parser.add_argument("-o", nargs=1, type=str, metavar="OUTFILE", default=['out.yml'])
parser.add_argument("-i", action="store_true", help="Edit original file and ignore outfile even if set.")
parser.add_argument("infile", metavar="INFILE")


args = parser.parse_args()

filename_input = args.infile


def _traverse_find(x, stk):
    #print("*********************************")
    #PP(x)
    #PP(stk)
    if len(stk) == 1:
        return x[stk[0]]
    else:
        return _traverse_find(x[stk[0]], stk[1:])

def far(data, stk, p_str, r_str):
    list_root = _traverse_find(data, stk)
    #PP(list_root)
    i=0
    for x in list_root:
        if x.startswith(p_str):
            list_root[i] = r_str
        i+=1

def dfl(data, stk, p_str, r_str):
    """Drop from list by prefix.
    """
    pass

def yset(data, stk, v_str):
    root = _traverse_find(data, stk[:-1])
    root[stk[-1]] = v_str

def yaddnull(data, stk):
    root = _traverse_find(data, stk[:-1])
    root[stk[-1]] = None

def yunset(data, stk):
    root = _traverse_find(data, stk[:-1])
    del root[stk[-1]]



x = yaml.safe_load(open(filename_input, 'r'))

if args.far is not None:
    prefix, stack, repl = args.far
    far(x, stack.split(","), prefix, repl)

if args.set is not None:
    stack, v = args.set
    yset(x, stack.split(","), v)

if args.unset is not None:
    stack = args.unset[-1]
    yunset(x, stack.split(","))

if args.addnull is not None:
    stack = args.addnull[-1]
    yaddnull(x, stack.split(","))


filename_output = args.o[-1]
if args.i:
    print("overwriting original")
    filename_output = filename_input

with open(filename_output, 'w') as f:
    f.write(yaml.safe_dump(x))

sys.exit(0)
