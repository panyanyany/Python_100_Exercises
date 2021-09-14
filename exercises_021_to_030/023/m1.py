import os
from pathlib import Path

from fpdf import FPDF

source_dir = Path('./storage')
print('目录 %s 下有文件：' % source_dir)
images = list(source_dir.glob('*.jpg'))
for name in images:
    print(name)

result_dir = Path('./result')
if not result_dir.exists():
    result_dir.mkdir(parents=True)

pdf = FPDF(format='A4')
for image in images:
    pdf.add_page()
    pdf.image(str(image), x=0, y=0, w=210, h=297)

dest = os.path.join(result_dir, "book.pdf")
pdf.output(dest)
print('输出到：', dest)
