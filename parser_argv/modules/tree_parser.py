#/usr/bin/python3

import sys
import re
import json

def treeParser(argv:list):
    unclear_arg = " ".join(argv)
    arg = re.split(r" -{1,2}", unclear_arg)
    
    all_argv = {}

    for _argv in arg:
        _content = _argv.split(" ")
        _arg = _content[0]
        if len(_content[1:]) == 1:
            _value = _content[1]
        else:
            _value = _content[1:] if len(_content[1:]) >= 1 else None
        
        all_argv[_arg] = _value

    return all_argv

if __name__ == "__main__":
    print(json.dumps(treeParser(), indent=2))
