# /usr/bin
# ---coding:utf-8---


class Animal():
    foot = 4

    __mouth = 1

    @classmethod
    def run(cls):
        print 'Animal run'

    def __init__(self, name):
        self.__name = name

    def eat(self):
        print 'Animal Eat'


class Person(Animal):

    @classmethod
    def run(cls):
        print 'Person run'

    def __init__(self, name, sex):
        Animal.__init__(self, name)
        self.sex = sex


    def eat(self):
        print 'Person Eat'

P = Person('XiaoMing', 'F')

P.run()

print P.foot
