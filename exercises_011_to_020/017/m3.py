import sys


def print2(*args, sep=' ', end='\n', file=sys.stdout):
    file.write(sep.join(args) + end)


print2('hello', 'world', file=open('out.txt', 'w+'))
