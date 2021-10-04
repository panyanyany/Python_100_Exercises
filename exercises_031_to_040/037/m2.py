class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


class MyClass2(object):
    pass


a = MyClass('hello')
b = MyClass('world')  # world 会覆盖 hello

print('a.name', a.name)  # 输出 world
print('b.name', b.name)
print('type(MyClass2)', type(MyClass2))
print('type(MyClass)', type(MyClass))
