total = 0
# range(1, 5) 会产生: 1, 2, 3, 4
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 为了避免某个数重复出现，如：1 2 1
            if i != j and j != k and k != i:
                print(i, j, k)  # 输出排列
                total += 1

print('total:', total)
