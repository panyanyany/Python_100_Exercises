import sys


def print2(*args, sep=' ', end='\n', out=sys.stdout):
    out.write(sep.join(map(str, args)) + end)


print2('hello', 'world', out=open('out.txt', 'w+'))
