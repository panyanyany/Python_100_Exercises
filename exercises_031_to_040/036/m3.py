class TestClass:
    pass


v1 = 1
v2 = 1.0
v3 = 'hello'
v4 = TestClass()

print('isinstance(v1, int) = {}'.format(isinstance(v1, int)))
print('isinstance(v2, float) = {}'.format(isinstance(v2, float)))
print('isinstance(v3, str) = {}'.format(isinstance(v3, str)))
print('isinstance(v4, TestClass) = {}'.format(isinstance(v4, TestClass)))
print('isinstance(v4, TestClass) = {}'.format(isinstance(TestClass, TestClass)))
