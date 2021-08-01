print(*(binary for binary in input().split(',') if int(binary, base=2) % 5 == 0))
