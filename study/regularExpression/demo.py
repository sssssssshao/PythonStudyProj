"""
    re模块
"""
s = 'ABC\\-001'  # python字符串
# 对应的正则表达式字符串编程：
# 'ABC|-001'
# 使用Python的r前缀，就不用考虑转义的问题了
s = r'ABC\-001'

print('--------------re模块---------------')
import re
print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}', '010 12345'))

print('--------------切分字符串---------------')
print('a b  c'.split(' '))
print(re.split(r'\s+', 'a b  c'))
print(re.split(r'[\s\,]+', 'a, b, c  d'))
print(re.split(r'[\s\,\;]+', 'a, b, c;;  d'))

print('--------------分组---------------')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups(), m.group(0), m.group(1), m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]'
             r'|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

print('--------------贪婪匹配---------------')
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

print('--------------编译---------------')
# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

print('--------------练习1---------------')


def is_valid_email(addr):
    re_email = re.compile(r'^[0-9a-zA-Z\.]+@[a-z]+(.com)$')
    return re_email.match(addr)


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


print('--------------练习2---------------')


def name_of_email(addr):
    re_email = re.compile(r'^(<?)([a-zA-Z\s]*)(>?)(\s?)(\w*)@(\w+)((.org)|(.com))$')
    return re_email.match(addr).group(2)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('tom@voyager.com') == 'tom'
print('ok')