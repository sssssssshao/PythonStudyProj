# if

age = int(input("age: "))
if age >= 18:
    print("your age is", age)
elif age >= 6:
    print("未成年")
else:
    print("儿童")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if 1:
    print('只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。')

height = 1.75
weight = 80.5
bmi = weight / pow(height, 2)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')