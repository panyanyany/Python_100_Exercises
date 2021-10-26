import os


def search(root, name):
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            # 忽略大小写
            if name in filename.lower():
                yield os.path.join(dirpath, filename)


for result in search('/usr/local', 'system'):
    print(result)
print(len(list(search('/usr/local', 'system'))))
