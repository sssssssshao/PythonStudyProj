# 高级特性
# Python中，代码越少越好,越简单越好。代码越少,开发效率越高
L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2


# print(L)


# 切片(Slice)操作符
# tuple也是 list，唯一区别就是 tuple不可变。结果仍是 tuple
# 字符串也可以看成 list,每个元素就是一个字符。结果仍是字符串
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3], L[:2], L[-2:])

L = list(range(100))
print(L[:10], L[-10:])  # 前十 后十
print(L[:10:2], L[::5])  # 前十个数,每两个取一个 所有数，每5个取一个
print(L[:])  # 原样复制一个 list

print((1, 2, 3, 4, 5)[:4], 'ABCDEFG'[:3])


def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# 迭代
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable), isinstance([1, 2, 3], Iterable), isinstance(123, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)


def findMinAndMax(L):
    if L:
        min, max = L[0], L[0]
        for value in L:
            if value < min:
                min = value
            if value > max:
                max = value
        return (min, max)
    else:
        return (None, None)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print(list(range(1, 11)))  # 生成1-10
print([x * x for x in range(1, 11)])  # 生成[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11) if x % 2 == 0])  # 筛选出仅偶数的平方
print([m + n for m in 'ABC' for n in 'XYZ'])  # 还可以使用两层循环，可以生成全排列

import os  # 导入os模块
print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'X', 'y': 'Y', 'z': 'Z'}
for k, v in d.items():
    print(k, '=', v)
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print([x * x for x in range(10)])
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
g = (x * x for x in range(10))
for n in g:
    print(n)

print('----------斐波拉契数列----------')


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)

print('----------generator斐波拉契数列结束---------')


# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)


print('----------斐波拉契数列结束---------')


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()
print('第一次', next(o))
print('第二次', next(o))
print('第三次', next(o))

print('----------获取 generator 的 return 值---------')
g = fib(6)
while True:
    try:
        print('g:', next(g))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


# 迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。可以使用isinstance()判断一个对象是否是Iterable对象
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
print('-------------迭代器-----------')
from collections import Iterator
print(isinstance((x for x in range(1, 10)), Iterator), isinstance([], Iterator), isinstance({}, Iterator), isinstance('abc', Iterator))
print(isinstance(iter([]), Iterator), isinstance(iter({}), Iterator), isinstance(iter('abc'), Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的
# 以下 for 和 使用Iterator循环是完全等价的
for x in [1, 2, 3, 4, 5]:
    print(x)

# 首先获得 Iterator 对象
it = iter([1, 2, 3, 4, 5])
# 循环：
while True:
    try:
        print(next(it))
    except StopIteration as e:
        # 遇到StopIteration就退出循环
        break

