import os

# 返回文件信息
print(os.stat(__file__))
# 抛出异常
print(os.stat('/path/to/file'))
