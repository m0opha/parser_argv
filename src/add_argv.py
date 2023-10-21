from useful_functions.json_print import json_print


import sys

def add_argument(*args,values=None,help=None,type=None,name=None, argv_before=None) -> dict:
    """
    Add arguments to the parser.

    :param args: The arguments to be added. Accepts multiple argument names.
    :param values: The maximum number of values expected for the argument. Default is one.
    :param type: Specify the expected data type (e.g., str, int, list).
    :param name: The name of the variable to store the argument.

    Raises:
        Error: If no arguments are provided or if there are repeated arguments in *args.
    """

    if len(args) == 0:
        print("[-] you have not given any argument")
        sys.exit()

    if argv_before == None:
        argv_before = {}

    if values == None:
        values = 1


    if type == None:
        type = str



    # search for repited args in *args
    repited_arg_in_args = []
    for _args in args:
        if _args in repited_arg_in_args:
            print(f"[-] {args} repeated arguments")
        repited_arg_in_args.append(_args)


    #define the name of the variable name
    if name == None:
        # delete the "-" from arguments
        arguments = []
        for _args in args:

            args_without_hypen = ""
            for _char in _args:
                if _char == "-":
                    continue

                args_without_hypen += _char	
            arguments.append(args_without_hypen)
    
        name = ""
        for _length in arguments:
            if len(name) < len(_length):
                name = _length

        #detect if some arg not start with -
        for _args in args:
                if _args[0] != "-":
                    print(f'[-] "{ _args }" -> arguments need to start with hyphen')
                    sys.exit()



    if argv_before != None:

        # seach for repited argument
        if argv_before != None:
            repited = 0
            for _variables in argv_before.keys():
                for _argument in args:
                    if _argument in argv_before[_variables]["args"]:

                        print(f'[-] Repited arguments "{_argument}" in "{_variables}, please change the names of one"')
                        repited += 1
            if repited > 0:
                sys.exit()

        if argv_before != None and name in argv_before:
            print(f'[-] The variable name "{name}" alreay exists')
            sys.exit()

        else:
            argv_before[name] = {
                "args": args,
                "type": type,
                "values": values,
                "help": help,
                }
        
        return argv_before
    
    else:

        argv_before[name] = {
                "args": args,
                "type": type,
                "values": values,
                "help": help,
                }
        
        return argv_before
    

if __name__ == "__main__":
    arguments = None
    arguments = add_argument("--hola","--hello",type=str,values=3, help="say hi", argv_before=arguments)
    arguments = add_argument("--chao","--goodbye",type=str,values=4,help="say bye ",argv_before=arguments)

    json_print(arguments)


