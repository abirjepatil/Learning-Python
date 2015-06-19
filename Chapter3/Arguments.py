#How to call a python program with arguments
#python test.py arg1 arg2 arg3
#First Argument is always the script name

import sys

print 'Number of arguments:', len(sys.argv), 'arguments'
print 'Argument List', str(sys.argv)

