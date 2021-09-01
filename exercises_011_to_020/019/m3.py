from pathlib import Path

my_file = Path(__file__)
# 解析成功，返回绝对路径
try:
    abs_path = my_file.resolve(strict=True)
    print('文件存在', abs_path)
except:
    print('文件不存在')

my_file = Path("/path/to/file")
# 解析失败，抛出异常
try:
    my_file.resolve(strict=True)
    print('文件存在')
except:
    print('文件不存在')
