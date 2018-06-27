# 序列化
"""
    我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
    在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

    序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
    Python提供了pickle模块来实现序列化。
"""

# 首先，我们尝试把一个对象序列化并写入文件：
import pickle
d = dict(name='Bob', age=20, score=80)

# pickle.dumps()方法把任意对象序列化成一个bytes，
# 然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()


# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
# 我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open('dump.txt', 'rb')
e = pickle.load(f)
f.close()
print('d:', d, '反序列化后的结果:', e)


# JSON
"""
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

            JSON类型	        Python类型
              {}	          dict
              []	          list
            "string"	      str
            1234.56	        int或float
            true/false	    True/False
              null	          None

由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
"""

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
d = dict(name='shao', age=20, score=99)
result = json.dumps(d)
print('将对象转换成 json：', type(result), result)

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

json_str = '{"name": "shao", "age": 20, "score": 99}'
result = json.loads(json_str)
print('读取json并转换成string ：', type(result), result)


# JSON进阶
"""
    Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象.
    错误的原因是Student对象不是一个可序列化为JSON的对象。
    如果连class的实例对象都无法序列化为JSON，这肯定不合理！
    别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
    https://docs.python.org/3/library/json.html#json.dumps
    这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
    可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
"""
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        "name": std.name,
        "age": std.age,
        "score": std.score
    }


s = Student('shao', 20, 11)
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print('class 序列化为 JSON:', json.dumps(s, default=student2dict))

result = json.dumps(s, default=lambda obj: obj.__dict__)
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
print('把任意 class 的实例变为 dict：', result)

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
#
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


std = json.loads(result, object_hook=dict2student)
print('将 JSON 反序列化为Student:', std, std.name, std.age, std.score)


obj = dict(name='小明', age=20, des='12')
s = json.dumps(obj, ensure_ascii=True)
print(s)

