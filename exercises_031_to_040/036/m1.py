class TestClass:
    pass


v1 = 1
v2 = 1.0
v3 = 'hello'
v4 = TestClass()

print('type(v1) = {}'.format(type(v1)))
print('type(v2) = {}'.format(type(v2)))
print('type(v3) = {}'.format(type(v3)))
print('type(v4) = {}'.format(type(v4)))
print('type(TestClass) = {}'.format(type(TestClass)))

print('-' * 20)

print('type(v1) is int = {}'.format(type(v1) is int))
print('type(v1) is float = {}'.format(type(v1) is float))

print('type(v4) is TestClass = {}'.format(type(v4) is TestClass))
