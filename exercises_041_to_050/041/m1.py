class StudentBase:
    name: str
    score: float

    def __init__(self, name, score):
        self.name = name
        self.score = score


class Student(StudentBase):
    def __str__(self):
        return f'{self.name}：{self.score}分'


# 直接输出对象的 id 信息
print(StudentBase('mike', 70))
# <__main__.StudentBase object at 0x10bf29f70>

# 输出自定义的、适合人类阅读的信息
print(Student('mike', 70))
# mike：70分

# 在容器中不会调用 __str__
print([Student('mike', 70), Student('john', 60)])
# [<__main__.Student object at 0x10a631fa0>, <__main__.Student object at 0x10a631e50>]
