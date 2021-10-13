from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int

    def __lt__(self, other):
        return self.age < other.age


li = [Student('小明', 11), Student('小红', 12),
      Student('小青', 9)]

li.sort()

print(li)
