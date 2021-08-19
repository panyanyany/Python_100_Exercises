import sys


def print2(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)


print2('hello', 'world', sep='===')
