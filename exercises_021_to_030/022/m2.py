import os
import shutil
from pathlib import Path

source_dir = Path('./storage')
print('目录 %s 下有文件：' % source_dir)
for obj in source_dir.iterdir():
    print(obj.name)

print()

result_dir = Path('./result')
if not result_dir.exists():
    result_dir.mkdir(parents=True)

for i, obj in enumerate(source_dir.iterdir()):
    new_name = '%03d' % i + obj.suffix
    print('正在重命名：%s --> %s' % (obj.name, new_name))

    new_obj = Path(result_dir.joinpath(new_name))

    shutil.copy(str(obj), str(new_obj))
