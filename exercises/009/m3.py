words = input('请输入多个单词：').split()

uniq_words = []

for w in words:
    if uniq_words.count(w) == 0:
        uniq_words.append(w)

uniq_words.sort()
print(" ".join(uniq_words))
