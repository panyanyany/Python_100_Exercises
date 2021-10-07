tu = ('Ming', 'Li')
li = ['Hong', 'Xiao']

score = {}

score[tu] = 95
try:
    # list 是可变的，所以不能作为 key
    score[li] = 60
except Exception as e:
    print(e)

print(score)
