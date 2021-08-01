words = input('请输入多个单词：').split(' ')

uniq_words = list(set(words))

uniq_words.sort()
print(' '.join(uniq_words))
