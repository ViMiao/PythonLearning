import shelve
db = shelve.open('class-shelve')
sue = db['sue']
sue.giveRaise(0.23)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(0.2)
db['tom'] = tom
db.close()