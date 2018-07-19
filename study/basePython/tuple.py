# tuple 元组:一旦初始化就不能修改
classmates = ('shao', 'feng', 'yi')
print(classmates)

# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
# 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1)
print(t)

t = (1,)
print(t)

# 元组中存在列表时,列表是可变的
t = (1,2,3,[22,3,4,5])
print(t)

t[-1][1] = 's'
t[-1][2] = 'f'
print(t)

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
print(L[-1][-1])