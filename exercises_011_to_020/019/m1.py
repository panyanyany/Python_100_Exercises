import os.path

# false
print(os.path.isfile('/path/to/file'))
# true
print(os.path.isfile(__file__))
