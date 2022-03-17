# python program
# command line arguments

import sys

# reverse arugment making use of "list slicing operator"

args = sys.argv[1:]
args_strings = " ".join(args)
reversed_args_strings = args_strings[::-1]
print(" " + reversed_args_strings)
