# 面向对象编程
"""
    面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

    面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

    而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

    在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

    面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。

    所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

    面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

    类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

    方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

    通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

    和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s的成绩 %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


print('--------------------类和实例--------------------')
"""
    面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
    比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
    
    和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
    除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
"""


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。


class Student(object):
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    # 特殊方法“__init__”前后分别有两个下划线！！！
    pass


bart = Student()
print(bart)  # 变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
bart.name = 'shao'  # 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
print(bart.name)
"""
    注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

    有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
"""


class Student(object):
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    # 特殊方法“__init__”前后分别有两个下划线！！！
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('shao', 99)
print(bart.name, bart.score)


print('--------------------数据封装--------------------')
"""
    面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。
    
    但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
    这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
    
    要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
"""
print(bart.get_grade())
bart.score = 60
print(bart.get_grade())


print('--------------------访问限制--------------------')
"""
    如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
    在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    
    在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
    特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    
    有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
    但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    
    双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
    不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
    但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s的成绩：%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


bart = Student('shao', 76)
bart.print_score()
bart.set_name('ss')
bart.set_score(88)
bart.print_score()
print(bart._Student__name)  # 不同版本的Python解释器可能会把__name改成不同的变量名。


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


print('--------------------继承和多态--------------------')
"""
    在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
    而被继承的class称为基类、父类或超类（Base class、Super class）。
"""


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


Animal().run()
Dog().run()
Cat().run()

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
print(isinstance(a, list), isinstance(b, Animal), isinstance(c, Dog), isinstance(c, Animal), isinstance(b, Dog))


def run_once(animal):
    animal.run()


run_once(Animal())
run_once(Dog())
run_once(Cat())


print('--------------------静态语言 vs 动态语言--------------------')
"""
    对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    
    Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
    但是，许多对象，只要有read()方法，都被视为“file-like object“。
    许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
"""


class Timer(object):
    def run(self):
        print('Start....')


run_once(Timer())


print('--------------------获取对象信息--------------------')
"""
    判断对象类型，使用type()函数，返回对应的Class类型
    判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
"""
print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
print(type(Timer()))
"""
    判断class的类型:isinstance()函数
    isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
    
    总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
"""
print(isinstance([1, 2, 3], (list, tuple)))

"""
    如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
    
    类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
    在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
    
    仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
    
    通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
"""
print(dir('123'))
print(len('123'))  # len()和'123'.__len__()  是等价的


class MyDog(object):
    def __len__(self):
        return 23


print(len(MyDog()))
print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性 x 吗？
print(obj.x)
print(hasattr(obj, 'y'))  # 有属性 y 吗？
setattr(obj, 'y', 19)  # 设置属性 y
print(hasattr(obj, 'y'))  # 有属性 y 吗？
print(getattr(obj, 'y'))  # 获取属性 y
print(obj.y)  # 获取属性 y
# getattr(obj, 'z')  # 获取不存在的属性会抛出AttributeError错误
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
print(hasattr(obj, 'power'))  # 有属性 power 吗
print(getattr(obj, 'power')())  # 有属性 power 吗


print('--------------------实例属性和类属性--------------------')


class Student(object):
    std_name = 'shao'  # 类属性

    def __init__(self, name):
        self.name = name


s = Student('feng')
print(s.std_name, s.name, Student.std_name)




