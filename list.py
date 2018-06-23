# list 列表
classmates = ['shao', 'feng', 'yi']
print(classmates)

print(len(classmates))

print(classmates[0])

print(classmates[-1])

# 将元素追加到 list
classmates.append('chen')

print(classmates)

# 将元素加到指定位置
classmates.insert(2, 'jiong')

print(classmates)

# 删除末尾元素
classmates.pop()
print(classmates)

# 删除指定位置元素
classmates.pop(1)
print(classmates)

# 指定位置元素替换
classmates[2] = ['feng', 'yi']
print(classmates)

