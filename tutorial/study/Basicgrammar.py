# -*- coding: utf-8 -*-
# print('I\'m ok.')
# print('\\\n\\')
# #如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
# print(r'\\\t\\')
# #如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
# print('''line1
# ... line2
# ... line3''')
# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)
# print ('growth rate: %d %%' % 7)
# print ('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])