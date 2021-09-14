from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def add_text(image_file: Path):
    my_image = Image.open(str(image_file))
    # 图像先转为 RGBA 图像
    image_layer = my_image.convert('RGBA')

    # 生成与主图片同等大小的图片
    text_layer = Image.new('RGBA', image_layer.size, (255, 255, 255, 0))
    text_canvas = ImageDraw.Draw(text_layer)

    # 指定字体和字体大小
    font = ImageFont.truetype('./font/sarasa-mono-sc-nerd-regular.ttf', 100)
    text = '@写代码的安徒生'
    # 获取文本尺寸
    text_size_w, text_size_h = text_canvas.textsize(text, font=font)
    # 设置文字位置
    text_pos = (image_layer.size[0] / 2 - text_size_w / 2, image_layer.size[1] / 2 - text_size_h / 2)
    # 把文字画上去
    text_canvas.text(text_pos, text, font=font, fill=(255, 255, 255, 70))

    # 将文字图片覆盖到主图片上
    new_image = Image.alpha_composite(image_layer, text_layer)

    # 压缩一下
    # new_image = new_image.quantize(method=2)

    save_to = Path('./result/' + image_file.name)
    if not save_to.parent.exists():
        save_to.parent.mkdir(parents=True)

    new_image.convert('RGB').save(save_to)


for item in Path('./image').glob('*.jpg'):
    add_text(item)
