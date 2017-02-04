import shelve
from person import Person
from manager import Manager
bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)
db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
# print(db['bob'])
db.close()