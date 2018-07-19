# 函数
import math

# 绝对值
print(abs(-10))

# 最大值
print(max(1, 2, 3, 4, 6, 7))

# 数据类型转换
print(int('123'))

print(float('12.2'))

print(str(12.1))

print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs  # 变量a指向abs函数
a(-1)  # 所以也可以通过a调用abs函数

n1 = 255
n2 = 1000
print(hex(255), hex(1000))


def my_abs(x):
    if not isinstance(x, (int, float)):  # 参数检查
        raise TypeError('参数类型错误')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-11))
# print(my_abs('11'))


def nothing():  # 空函数
    pass  # 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。


# 返回多个值
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y, move(100, 100, 60, math.pi / 6))


def quadratic(a, b, c):
    num = math.sqrt(abs(4 * a * c - b * b))
    return (-b + num)/(2 * a), (-b - num)/(2 * a)


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(x, n=1):
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result


print(power(2))
print(power(2, 2))


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，
# 不再是函数定义时的[]了。
# 默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())  # 因为 None是不变对象，所以无论执行多少次都只会有1个 END
print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc())
print(calc(1, 2, 3, 4))
nums = [1, 2, 3, 4]
print(calc(*nums))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('shao', 20)
person('feng', 10, city='wenzhou')
extra = {'city': 'wenzhou', 'job': 'IT'}
person('yi', 5, **extra)


# 命名关键字参数
# 只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('shao', 11, city='wenzhou', job='iT')


# 如果函数定义中已经有了一个可变参数，
# 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *arg, city, job):
    print(name, age, arg, city, job)


person('shao', 11, 23, 24, city='wenzhou', job='iT')


def product(num1, *otherNum):
    sum = num1
    for n in otherNum:
        sum = sum * n
    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# 递归函数
# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 解决递归调用栈溢出的方法是通过尾递归优化，尾递归和循环的效果是一样的，所以可以把循环看成是一种特殊的尾递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(9))
# print(fact(1000))   会出现栈溢出


# 尾递归：在函数返回的时候，调用自身本身，并且 return 语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# print(fact_iter(100, 1))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 把a从第一个到第n-1个放到b
        move(1, a, b, c)  # 把a中的第n个放到c
        move(n - 1, b, a, c)  # 把b中的 n-1个放到c


move(3, 'A', 'B', 'C')

