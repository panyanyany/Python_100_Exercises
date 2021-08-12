words = input('输入文本：').split()
freq = {}
for word in set(words):
    freq[word] = words.count(word)

words = list(freq.items())
words.sort(key=lambda e: e[1])

for w in words:
    print("%10s: %d" % w)
