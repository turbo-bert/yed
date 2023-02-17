import argparse
import yaml
from pprint import pprint as PP

filename_input = "in.yml"
filename_output = "out.yml"

def _traverse_find(x, stk):
    #print("*********************************")
    #PP(x)
    #PP(stk)
    if len(stk) == 1:
        return x[stk[0]]
    else:
        return _traverse_find(x[stk[0]], stk[1:])

def update_listitem_by_prefix(data, stk, p_str, r_str):
    list_root = _traverse_find(data, stk)
    #PP(list_root)
    i=0
    for x in list_root:
        if x.startswith(p_str):
            list_root[i] = r_str
        i+=1

x = yaml.safe_load(open(filename_input, 'r'))
#PP(x)
update_listitem_by_prefix(x, ["service", "db", "env"], "A=", "A=ersetzt")


with open(filename_output, 'w') as f:
    f.write(yaml.safe_dump(x))
