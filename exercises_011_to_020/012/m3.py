line = input('输入密码：')


def is_valid(password: str):
    has_lower_letter = False
    has_upper_letter = False
    has_number = False
    has_symbol = False
    has_length = False
    has_invalid = False
    reasons = []

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
        else:
            has_invalid = True

    if 6 <= len(password) <= 12:
        has_length = True

    if not has_lower_letter:
        reasons.append('至少包含一个小写字母')
    if not has_upper_letter:
        reasons.append('至少包含一个大写字母')
    if not has_number:
        reasons.append('至少包含一个数字')
    if not has_symbol:
        reasons.append('至少包含一个特殊符号')
    if not has_length:
        reasons.append('长度要在6~12')
    if has_invalid:
        reasons.append('包含非法字符')

    return all([
        has_lower_letter,
        has_upper_letter,
        has_number,
        has_symbol,
        has_length,
        not has_invalid,
    ]), reasons


valid, reasons = is_valid(line)
print(valid)
print('======')
print('\n'.join(reasons))
