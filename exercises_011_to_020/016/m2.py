score = int(input('输入成绩:'))
standard = [
    (90, 'A'),
    (60, 'B'),
    (0, 'C'),
]
grade = None
for item in standard:
    if score >= item[0]:
        grade = item[1]
        break

print('%d 属于 %s' % (score, grade))
