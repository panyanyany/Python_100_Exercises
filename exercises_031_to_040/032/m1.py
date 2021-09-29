class People:
    Type = '人'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'{self.name} 是 {self.Type}')


class Teacher(People):
    pass


class Student(People):
    pass


teacher_li = Teacher('李老师')
student_ming = Student('小明')
student_hong = Student('小红')

print('------ 1')
teacher_li.show()
student_ming.show()
student_hong.show()

print('------ 2')
People.Type = '僵尸'

teacher_li.show()
student_ming.show()
student_hong.show()

print('------ 3')
People.Type = '人'
Student.Type = '僵尸'

teacher_li.show()
student_ming.show()
student_hong.show()

print('------ 4')
People.Type = '人'

teacher_li.show()
student_ming.show()
student_hong.show()
