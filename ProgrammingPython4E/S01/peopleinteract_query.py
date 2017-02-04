# interactive queries
import shelve
fieldname = ('name', 'age', 'pay', 'job')
maxfield = max(len(f) for f in fieldname)
db = shelve.open('class-shelve')
while True:
    key = (input('\nkey? = > '))
    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldname:
            print(field.ljust(maxfield), '=>', getattr(record, field))