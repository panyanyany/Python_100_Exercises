words = input('输入文本：').split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

words = list(freq.items())
words.sort(key=lambda e: e[1])

for w in words:
    print("%10s: %d" % w)
