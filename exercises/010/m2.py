s = input('输入一行字符串：')
stat = {"DIGITS": 0, "LETTERS": 0}

for c in s:
    if c.isdigit():
        stat['DIGITS'] += 1
    elif c.isalpha():
        stat['LETTERS'] += 1
    else:
        pass

print(stat)
