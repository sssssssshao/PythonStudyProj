# 循环

# for 循环
names = ['shao', 'feng', 'yi']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)

print(list(range(5)))

# 0-100相加
sum = 0
for x in range(101):
    sum += x
print(sum)

# while 循环
sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,',x)

# break
print('break Start')
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('break End')

# continue
print('continue')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
