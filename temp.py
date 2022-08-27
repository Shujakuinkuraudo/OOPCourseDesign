class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print("parent的init开始被调用")
        self.name = name
        print("parent的init结束被调用")


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son1的init开始被调用")
        self.age = age
        super().__init__(name, *args, **kwargs)
        print("Son1的init结束被调用")


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print("Son2的init开始被调用")
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print("Son2的init结束被调用")


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson的init开始被调用")
        # 多继承时,相对于实用类名.__init___方法, 要把每个父类全部写一遍
        # 而super只用一句话,执行全部父类的方法,这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender)
        super().__init__(name, age, gender)
        print("Grandson的init结束被调用")
        
a = Grandson("123",1,12)
print(a.gender,a.age)

        