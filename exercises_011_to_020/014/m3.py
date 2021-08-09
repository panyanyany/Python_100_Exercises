class MyRange:
    def __call__(self, n):
        i = 0
        while i < n:
            yield i
            i += 1


my_range = MyRange()

for i in my_range(10):
    print(i)
