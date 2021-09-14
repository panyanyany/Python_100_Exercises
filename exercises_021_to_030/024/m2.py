class MySum:
    def __call__(self, *args):
        if (len(args) == 1 and
           isinstance(args[0], list)):
            args = args[0]
        total = 0
        for item in args:
            total += item
        return total


mysum = MySum()
print(mysum([1, 2, 3]))
print(mysum(1, 2, 3))
