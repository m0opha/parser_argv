import sys
import json

def parser():

    arg_extract = {}
    key = "filename"
    value = []
    set_file_name = True

    for _args in sys.argv:
        if _args[0] == "-":
            if key != _args:
                if value == []:
                    arg_extract[key] = None
                else:
                    arg_extract[key] = value if len(value) > 1 else value[0]
                    value = []
            key = _args

        else:
            
            if set_file_name:
                set_file_name = False
                arg_extract[key] = _args
                key = "lonely_argv"
                value = []
                continue

            value.append(_args)

    if key:
        if value == []:
            arg_extract[key] = None
        else:
            arg_extract[key] = value if len(value) > 1 else value[0]

    return arg_extract

if __name__ == "__main__":
    print(json.dumps(parser(), indent=2))
