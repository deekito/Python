# /usr/bin
# -*-coding:utf-8-*-
import random

class NumberGuess():

    flag = True

    def __init__(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

N = NumberGuess(random.randint(0, 100))

print N.getNumber()

while(NumberGuess.flag):
    userGuess = int(raw_input('请输入一个0～100的数字:'))
    if userGuess > int(N.getNumber()):
        print '你猜的数字太大了'
        continue
    elif userGuess < int(N.getNumber()):
        print '你猜的数字太小了'
        continue
    else:
        print '你猜对了'
        NumberGuess.flag = False