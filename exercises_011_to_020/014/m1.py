def my_range(n):
    i = 0
    result = []
    while i < n:
        result.append(i)
        i += 1

    return result


for i in my_range(10):
    print(i)
