"""
person类的替代实现，包含数据、行为和运算符重载（未用于对象的持久储存）
"""
class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, persent):
        self.pay *= (1.0 + persent)
    def __str__(self):
        return ('<%s => %s: %s, %s>' %
                (self.__class__.__name__, self.name, self.job, self.pay))

class Manager(Person):
    """
    带有自定义加薪的Person
    继承了通用的lastName，str
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, persent, bouns = 0.1):
        Person.pay *= (1.0 + persent + bouns)

if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, sue):
        obj.giveRaise(0.1)
        print(obj)
