def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass(object):
    def __init__(self, name):
        self.name = name


class MyClass2(object):
    pass


a = MyClass('hello')
b = MyClass('world')

print('a.name', a.name)  # a.name hello
print('b.name', b.name)  # b.name hello
print('b is a', b is a)  # b is a True
print('type(MyClass2)', type(MyClass2))  # type(MyClass2) <class 'type'>
print('type(MyClass)', type(MyClass))  # type(MyClass) <class 'function'>
