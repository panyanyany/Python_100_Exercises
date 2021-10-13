l1 = [1, 2]
l2 = [2, 3]

# AND: 且操作符，只保留2个数组中 相同 的部分
same = list(set(l1) & set(l2))
# XOR: 异或操作符，只保留2个数组中 不同 的部分
diff = list(set(l1) ^ set(l2))

print('共有', same)
print('不同', diff)
