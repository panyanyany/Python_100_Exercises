class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


class MyClass2(object):
    pass


a = MyClass('hello')
b = MyClass('world')

print('a.name', a.name)
print('b.name', b.name)
print('type(MyClass2)', type(MyClass2))
print('type(MyClass)', type(MyClass))
