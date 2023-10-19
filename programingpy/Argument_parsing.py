import sys
import getopt

filename = 'test.txt'
message = 'hello'

opts, args = getopt.getopt(sys.argv[1:],'f:m:', ['filename','message'])

for opt , arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg 

with open(filename, 'w+') as f:
    f.write(message)