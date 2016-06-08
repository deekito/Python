#-*-coding:utf8-*-
'''
L = range(1,100)

print L

def X_3(x):
    if x % 3 == 0:
        return True
    else:
        return False

print filter(X_3, L)

print L
'''
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

print 'Bart' > 'Adam'

print type(p1.name)

L1 = [p1, p2, p3]
L2 = sorted(L1, key = lambda p:p.name, reverse=True)

print L2[0].name
print L2[1].name
print L2[2].name