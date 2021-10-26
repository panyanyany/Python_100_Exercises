import os
import zipfile

dirname = '/private/var/www/coding-anderson/Python_100_Exercises/exercises_031_to_040'


def zipdir(path, ziph: zipfile.ZipFile):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.py'):
                continue
            abspath = os.path.join(root, file)
            ziph.write(abspath,
                       # 必须传入相对路径，
                       # 否则压缩包里的文件夹是从 /private 开始的
                       os.path.relpath(abspath,
                                       os.path.join(path, '..')))


zipf = zipfile.ZipFile('my_file.zip', 'w',
                       zipfile.ZIP_DEFLATED)
zipdir(dirname, zipf)
zipf.close()
