import sys


def print2(*args, end='\n'):
    sys.stdout.write(' '.join(args) + end)


print2('hello', 'world', end='\n\n\n')
print2('hello', 'world')
