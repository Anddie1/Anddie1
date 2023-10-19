import sys

arg1 = sys.argv[0]
arg2 = sys.argv[1]
arg3 = sys.argv[2]


with open(f'{arg2}', 'w+') as f:
    f.write(arg3)
    f.close()

print(arg2)