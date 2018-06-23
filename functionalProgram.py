# 函数式编程

# 高级函数


# abs函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-2, 4, abs))


# map 和 reduce
# map:map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce:reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4, 5]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(list(map(char2num, '12345')), reduce(fn, map(char2num, '12345')))


def str2int(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int('123456'))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('1234567'))


# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s.split('.')[0] + s.split('.')[1]))
    return result / pow(10, len(s.split('.')[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# filter
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素
print(list(filter(lambda n: n % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])))  # 删掉偶数，只保留奇数
print(list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '  '])))  # 把一个序列中的空字符串删掉


# 计算素数的一个方法是埃氏筛法
# 这是一个生成器，并且是一个无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
L = []
for n in primes():
    if n < 10:
        L.append(n)
    else:
        break


print('素数：', L)


print('123456'[::-1])


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(lambda n: str(n)[::1] == str(n)[::-1], range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


print('---------排序算法----------')
# 排序算法
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
# Python内置的sorted()函数就可以对list进行排序,sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda t: t[0]))
print(sorted(L, key=lambda t: t[1], reverse=True))
print(sorted(L, key=lambda t: -t[1]))


print('---------返回函数----------')
# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


# 闭包
# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def count():
    fs = []
    for n in range(1, 4):
        def f():
            return n * n
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())  # 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9


def count():
    fs = []
    for n in range(1, 4):
        fs.append((lambda i: lambda: i * i)(n))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 闭包返回一个计数器函数，每次调用它返回递增整数
print('----------通过函数----------')


def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


print('----------通过生成器----------')


def createCounter():
    def tempCounter():
        n = 1
        while True:
            yield n
            n += 1
    temp = tempCounter()
    return lambda: next(temp)


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


print('----------匿名函数----------')
# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。 lambda x: x * x
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f, f(5))
print(list(filter(lambda n: n % 2 == 1, range(1, 20))))


print('----------装饰器----------')
# 装饰器
# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
import functools


# 函数log是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
def log(func):
    @functools.wraps(func)  # wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 相当于执行了 now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
@log
def now():
    print('2018-06-22')


now()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        @functools.wraps(func)  # wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 相当于执行了 now = log('execute')(now)
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
@log('测试')
def now():
    print('2018-06-22')


now()


import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end_time - start_time) * 1000))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')


print('----------偏函数----------')
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))


# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(n, base=2):
    return int(n, base)


print('二进制:', int2('100000101'))


# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools
int2 = functools.partial(int, base=2)
print('functools.partial二进制:', int2('100000101'))  # 相当于 kw = { 'base': 2 }     int('10010', **kw)

max2 = functools.partial(max, 10)  # 实际上会把10作为*args的一部分自动加到左边
print(max2(5, 6, 7))  # 相当于 args = (10, 5, 6, 7)  max(*args)



