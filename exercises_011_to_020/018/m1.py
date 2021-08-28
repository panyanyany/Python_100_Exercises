d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

for key in d2:
    d1[key] = d2[key]

print(d1)
