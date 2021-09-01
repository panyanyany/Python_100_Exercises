from pathlib import Path

# true
my_file = Path(__file__)
print(my_file.is_file())

# false
my_file = Path("/path/to/file")
print(my_file.is_file())
