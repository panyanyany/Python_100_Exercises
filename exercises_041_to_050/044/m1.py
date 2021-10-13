import re

line = '  ab\td\x00efg\n\n\n hi\nworld\t'
print(line)
print(repr(line))
# '  ab\td\x00efg\n\n\n hi\nworld\t'

line = '  ab\td\x00efg\n\n\n hi\nworld\t'
line = line.strip()
print(repr(line))
# 'ab\td\x00efg\n\n\n hi\nworld'

line = '  ab\td\x00efg\n\n\n hi\nworld\t'
line = re.sub(r'\s', '', line)
print(repr(line))
# 'abd\x00efghiworld'

line = '  ab\td\x00efg\n\n\n hi\nworld\t'
line = re.sub(r'(\s|\x00)', '', line)
print(repr(line))
# 'abdefghiworld'
