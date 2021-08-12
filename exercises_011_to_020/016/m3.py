score = int(input('输入成绩:'))
# 仅对 Python 3.7 及以上版本有效
standard = {
    90: 'A',
    60: 'B',
    0: 'C',
}
grade = None
for key_score in standard:
    if score >= key_score:
        grade = standard[key_score]
        break

print('%d 属于 %s' % (score, grade))
