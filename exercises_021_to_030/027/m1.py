from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def add_text(image_file: Path):
    my_image = Image.open(image_file)
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

    # 循环打印文字，让文字水印遍布图片
    for y in range(0, int(image_layer.size[1] - text_size_h), int(text_size_h + text_size_h * 2)):
        for x in range(0, int(image_layer.size[0] - text_size_w), int(text_size_w + text_size_w / 5)):
            # 设置文字位置
            text_pos = (x, y)
            # 把文字画上去
            text_canvas.text(text_pos, text, font=font, fill=(255, 255, 255, 50))

    # 把水印图层旋转45度
    text_layer = text_layer.rotate(45)

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
