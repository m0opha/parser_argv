#!/usr/bin/python3

import re
import json
import sys

from .modules import treeParser

#consumible functions
def removeCharacterText(text:str, character:str):
    final_text = ""
    for _w in text:
        if character == _w:
            continue
        final_text += _w

    return final_text

class ArgNotAdded(Exception):
    def __init__(self, arg:str):
        super().__init__(f"This arguments was never added \"{arg}\"")

        
class ParserArgv:
    def __init__(self) -> None:
        self.unclear_argv = sys.argv
        self.filename = self.unclear_argv[0]
        self.struct_arg = treeParser(self.unclear_argv)
        self.added_arg = {}
        var_asigned = {}
    
    def addArg(self,*arg, text_help="", accepted_values=1):
        possible_args = []
        for _a in arg:
            possible_args.append(removeCharacterText(_a,"-"))
        
        self.added_arg[possible_args[0]] = {
                                        "args":possible_args,
                                        "text_help":text_help,
                                        "accepted_values":accepted_values 
                                        }
        
    def getArgv(self):
        class arg:
            pass

        allowed_arg = self._workerGetAllowedArg(self.added_arg)

        for _arg , _value in self.struct_arg.items():
            if _arg not in allowed_arg:
                raise ArgNotAdded(_arg)
            
            if _arg == self.filename:
                setattr(arg, "free_value", _value)
                continue

            setattr(arg, self._workerReturnNameVar(_arg), _value)
        
        return arg

    #intern functions
    def _workerGetAllowedArg(self, added_arg:dict):
        #get all arguments allowed
        
        allowed_arg = [sys.argv[0], "help"]
        for _namekey , _value in self.added_arg.items():
            allowed_arg.extend(_value["args"])
        
        return allowed_arg

    def _workerReturnNameVar(self, arg):
        
        for _varname , _value in self.added_arg.items():
            if arg in _value["args"]:
                return _varname
           
if __name__ == "__main__":
    #usage
    parserargv = ParserArgv()
    parserargv.addArg("--host","-H", text_help="Setting up ip host")
    parserargv.addArg("--port", "-P", text_help="Seeting up port host")
    parserargv.addArg("--user", "-u")
    parserargv.addArg("--passwd", "-p")

    argv = parserargv.getArgv()

    #consume vars
    free_value = argv.free_value #there're arguments write at first and added here
    host = argv.host #the name for the variable is the first argument you add
    port = argv.port
    
    print(host)
    print(port)


   

