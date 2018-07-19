# 错误、调试和测试

# try
try:
    print('tye...')
    # r = 10 / 0
    r = 10 / int('a')
    # r = 10 / int('2')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    print('ValueError', e)
except Exception as e:
    print('BaseException...')
else:
    print('else...')
finally:
    print('finally...')
print('END')
