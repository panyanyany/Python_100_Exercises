l1 = [1, 2]
l2 = [2, 3]

same = []
diff = []
for item_1 in l1:
    if item_1 not in l2:
        diff.append(item_1)
    else:
        same.append(item_1)
for item_2 in l2:
    if item_2 not in l1:
        diff.append(item_2)
    else:
        same.append(item_2)

print('共有', same, list(set(same)))
print('不同', diff)