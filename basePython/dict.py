# dict 字典 键-值（key-value）存储
"""
dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
    第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
"""
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

d = {'shao': 100, 'feng': 90, 'yi': 80}
print(d['shao'])

d['feng'] = 95
print(d['feng'])

print('chen' in d)

print(d.get('yi'))
print(d.get('chen'))  # 返回None的时候Python的交互环境不显示结果。
print(d.get('chen', -1))

d.pop('shao')
print(d)

# set key的集合,没有重复的key
s = set([1, 2, 3])
print(s)

s.add(1)
print(s)
s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([2, 3, 4])
print(s & s1)  # 交集
print(s | s1)  # 并集

