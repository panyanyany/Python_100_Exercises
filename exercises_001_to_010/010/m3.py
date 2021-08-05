line = input('输入一行字符串：')

LETTERS, DIGITS = 0, 0

for i in line:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        LETTERS += 1
    if '0' <= i <= '9':
        DIGITS += 1

print("LETTERS", LETTERS)
print("DIGITS", DIGITS)
