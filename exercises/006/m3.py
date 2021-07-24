# 多行文本
class InputOutString:
    def __init__(self):
        self.s = ''

    def get_string(self):
        print('输入多行文本，最后一行输入END：')
        while True:
            tmp = input()
            if tmp == "END":
                break
            self.s += tmp + '\n'

    def print_string(self):
        print(self.s.upper())


str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()
