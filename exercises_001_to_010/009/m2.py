words = input('请输入多个单词：').split()

exists = {}

for w in words:
    exists[w] = True

words = list(exists.keys())

words.sort()
print(" ".join(words))
