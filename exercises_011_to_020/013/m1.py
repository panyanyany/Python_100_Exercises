lst = []
while True:
    s = input()
    if not s:
        break
    lst.append(s.split(','))

lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
for item in lst:
    print(item)
