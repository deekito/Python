class Person(object):

    address = 'Shanghai'

    def __init__(self, name):
        self.name = name

P = Person('Liwei')

P1 = Person('Henly')

P.address = 'Beijing'

print '%s:%s'%(P.name, P.address)

print '%s:%s'%(P1.name, P1.address)

print Person.address