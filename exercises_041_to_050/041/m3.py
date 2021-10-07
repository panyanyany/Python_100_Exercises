class Student:
    name: str
    score: float

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name},{self.score}分>'


# 没有 __str__ 的情况下，直接调用 __repr__
print(Student('mike', 70))
# <Student: mike,70分>


# 在容器中调用了 __repr__
print([Student('mike', 70), Student('john', 60)])
# [<Student: mike,70分>, <Student: john,60分>]
