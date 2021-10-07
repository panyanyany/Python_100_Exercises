class Student:
    name: str
    score: float

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name}：{self.score}分'

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name},{self.score}分>'


print(Student('mike', 70))
# mike：70分


# 在容器中调用了 __repr__
print([Student('mike', 70), Student('john', 60)])
# [<Student: mike,70分>, <Student: john,60分>]
