import os
from pathlib import Path

import pandas
import requests

xlsx = pandas.read_excel('./图片链接.xlsx')
for index, row in xlsx.iterrows():
    name = row['名称']
    url = row['图片链接']

    print(f'正在下载[{name}]：{url}')
    response = requests.get(url)

    basename, ext = os.path.splitext(url)
    if ext not in ['.jpg', '.png', '.jpeg', '.webp']:
        ext = '.jpg'

    filepath = Path(f'./storage/{name}{ext}')
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True)

    with filepath.open('w+b') as fp:
        fp.write(response.content)
