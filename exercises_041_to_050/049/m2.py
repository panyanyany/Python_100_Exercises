str1 = 'BUSSE'
str2 = 'Buße'

print(str1 == str2)
print(str1.lower() == str2.lower())
print(str1.casefold(), str2.casefold())
# 转换成：busse busse
print(str1.casefold() == str2.casefold())
# 结果：True
