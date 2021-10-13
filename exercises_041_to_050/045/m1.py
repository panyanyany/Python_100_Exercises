from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int


li = [Student('小明', 11), Student('小红', 12),
      Student('小青', 9)]

li.sort(key=lambda e: e.age)

print(li)

li = [Student('小明', 11), Student('小红', 12),
      Student('小青', 9)]
li2 = sorted(li, key=lambda e: e.age)
print(li)
print(li2)
