# /usr/bin
# -*-coding:utf-8-*-
import random


class NumberGuess():
    __flag = True

    @classmethod

    def __init__(self, number):
        self.__number = number

    def getnumber(self):
        return self.__number

    @property
    def flag(self):
        return self.__flag

    @__flag.setter
    def flag(self, value):
        if value:
            self.__flag = True
        else:
            self.__flag = False


N = NumberGuess(random.randint(0, 100))

while (NumberGuess.flag()):
    userGuess = int(raw_input('请输入一个0～100的数字:'))
    if userGuess > int(N.getnumber()):
        print '你猜的数字太大了'
        continue
    elif userGuess < int(N.getnumber()):
        print '你猜的数字太小了'
        continue
    else:
        print '你猜对了'
        NumberGuess.flag(False)

