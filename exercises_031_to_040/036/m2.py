class TestClass:
    pass


v1 = 1
v2 = 1.0
v3 = 'hello'
v4 = TestClass()

print('v1.__class__ = {}'.format(v1.__class__))
print('v2.__class__ = {}'.format(v2.__class__))
print('v3.__class__ = {}'.format(v3.__class__))
print('v4.__class__ = {}'.format(v4.__class__))

print('-' * 20)

print('v1.__class__ is int = {}'.format(v1.__class__ is int))
print('v1.__class__ is float = {}'.format(v1.__class__ is float))

print('v4.__class__ is TestClass = {}'.format(v4.__class__ is TestClass))
