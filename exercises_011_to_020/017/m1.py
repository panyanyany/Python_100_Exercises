import sys


def print2(*args, end='\n'):
    sys.stdout.write(' '.join(map(str, args)) + end)


print2('hello', 'world', end='\n\n\n')
print2('hello', 'world')
