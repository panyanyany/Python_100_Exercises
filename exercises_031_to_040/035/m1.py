from pathlib import Path

file_example = Path('./示例文件.txt')

with file_example.open() as fp:
    lines = fp.readlines()
    lines = [line.rstrip() for line in lines]
print('方法一：', lines)

# 适合读取大文件，比如 1G
with file_example.open() as fp:
    lines = []
    for line in fp:
        lines.append(line.rstrip())
print('方法二：', lines)

with file_example.open() as fp:
    lines = []
    while line := fp.readline():
        lines.append(line.rstrip())
print('方法三：', lines)
