#-*-coding:utf8-*-

def fun(f):
    def fun_1(*args):
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return f(args)
    return fun_1

def getSum(*args):
    return sum(*args)

g = fun(getSum)

print g(1,2,3,'3')