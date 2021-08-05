line = input('输入密码：')


def is_valid(password: str):
    has_lower_letter = False
    has_upper_letter = False
    has_number = False
    has_symbol = False
    has_length = False

    symbols = '`-=[]\\;\',./~!@#$%^&*()_+{}|:"<>?'

    for c in password:
        if c.islower():
            has_lower_letter = True
        elif c.isupper():
            has_upper_letter = True
        elif c.isnumeric():
            has_number = True
        elif c in symbols:
            has_symbol = True
        else:  # 避免其他符号，比如 emoji，中文，空格等
            return False

    if 6 <= len(password) <= 12:
        has_length = True
    return has_lower_letter and has_upper_letter and has_number and has_symbol and has_length


print(is_valid(line))
