from dryads import Dryads, DryadsFlag

cmd_tree = {
    "invalid-opt": DryadsFlag.AcceptArg,
}


Dryads(cmd_tree)

"""
> python flag_accept_arg_invalid.py      
...
Exception: [Drayd] DryadsFlag should not be used alone.
"""
