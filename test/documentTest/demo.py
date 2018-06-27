import re
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))


"""
    Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
    doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
"""


def myAbs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> myAbs(1)
    1
    >>> myAbs(-1)
    1
    >>> myAbs(0)
    0
    '''
    return n if n >= 0 else (-n)


sum = 1
for i in range(1, 10):
    sum *= i

print(sum)