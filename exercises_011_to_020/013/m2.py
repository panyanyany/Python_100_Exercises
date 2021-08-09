lst = []
while True:
    s = input()
    if not s:
        break
    lst.append(s.split(','))

lst.sort(key=lambda x: int(x[2]))
for item in lst:
    print(item)
