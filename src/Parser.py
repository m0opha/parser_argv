import sys
import json

def parser():

    arguments_tree= {}
    key = "filename"
    value = []

    set_filename = True

    for _args in sys.argv:
        if _args[0] == "-":
            if key != _args:
                if value == []:
                    arguments_tree[key] = None
                else:
                    arguments_tree[key] = value if len(value) > 1 else value[0]
                    value = []
            key = _args

        else:
            
            if set_filename:
                #save the path of executable file
                set_filename = False
                arguments_tree[key] = _args

                #change the flag for 
                key = "lone"
                value = []
                continue

            value.append(_args)

    #if a key remains put in the args
    if key:
        if value == []:
            arguments_tree[key] = None

        else:
            arguments_tree[key] = value if len(value) > 1 else value[0]


    return arguments_tree

if __name__ == "__main__":
    print(json.dumps(parser(), indent=2))
