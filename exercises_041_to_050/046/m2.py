from pathlib import Path


def search(root: Path, name):
    # rglob 无法忽略大小写
    yield from root.rglob(f'*{name}*')


for result in search(Path('/usr/local'), 'system'):
    print(result)
print(len(list(search(Path('/usr/local'), 'system'))))
