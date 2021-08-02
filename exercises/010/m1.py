line = input('输入一行字符串：')
DIGITS, LETTERS = 0, 0

for c in line:
    if c.isdigit():
        DIGITS += 1
    elif c.isalpha():
        LETTERS += 1
    else:
        pass

print("LETTERS", LETTERS)
print("DIGITS", DIGITS)
