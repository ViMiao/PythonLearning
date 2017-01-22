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


