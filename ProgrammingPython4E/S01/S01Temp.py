# -*- coding:utf-8 -*-

NAME, AGE, PAY, DEPARTMENT = range(4)
# bob = ['Bob Smith', 42, 30000, 'Software']
# sue = ['Sue Jones', 45, 40000, 'Hardware']
def splitLine(total = 1):
    for i in range(total):
        print('==========')

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]

people = [bob, sue]

for person in people:
    print(person[0][1], person[2][1])

splitLine()

print([person[0][1] for person in people])

splitLine()

for person in people:
    print(person[0][1].split()[-1])
    person[2][1] *= 1.10
    print(person[2])

splitLine(5)

for person in people:
    for (name, value) in person:
        if name == 'name': print(value)

def field(record, lable):
    for (fname, fvalue) in record:
        if fname == lable: return fvalue

print(field(bob, 'name'))
print(field(bob, 'age'))
print('a', 'b', 'c')

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'Job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 50000, 'Job': 'hardware'}

splitLine(3)
print(bob['name'], bob['pay'])
splitLine(1)
bob = dict(name = 'Bob Smith', age = 42, pay = 30000, job = 'dev')
print(bob['age'])

splitLine(2)
bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'Job': ['software', 'dev'],
        'pay': (30000, 50000)}
print(bob2)
splitLine(2)
print(bob2['name']['last'], bob2['Job'][1])
bob2['Job'].append('hardware')
print(bob2, 'pay: ', sum(bob2['pay']), sep= '\n')