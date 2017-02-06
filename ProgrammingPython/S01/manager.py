from person import Person
class Manager(Person):
    def giveRaise(self, percent, bonus = 0.1):
        self.pay *= (1.0 + percent + bonus)
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manage')

if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    print(tom.lastName())
    tom.giveRaise(0.20)
    print(tom.pay)
    tom = Manager('Tom Jones', 50)
    print(tom)