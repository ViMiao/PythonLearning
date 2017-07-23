"""
实现用来查看和更新保存在shelve中类实例的基于Web的界面；
shelve保存在服务器上（如果是本地机器的话就是同一个服务器）
"""
import cgi, shelve, sys, os                      #cgi.test()转储输入
shelvename = 'class-shelve'                     #shelve文件在当前工作目录
fieldnames = ('name', 'age', 'job', 'pay')
form = cgi.FieldStorage()                        #解析表单数据
print('Content-type: text/html')              #响应html中的hdr和空行
sys.path.insert(0, os.getcwd())                 #为了this和pickler查找person

#主html模板
replyHtml = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>People Input Form</title>
</head>
<body>
<form method="post" action="peoplecgi.py">
    <table>
        <tr><th>key<td><input type="text" name="key" value="%(key)s"></td></th></tr>
        $ROWS$
    </table>
    <p>
        <input type="submit" value="Fetch", name="action">
        <input type="submit" value="Update", name="action">
    </p>
</form>
</body>
</html>
"""

#为$ROWS$数据行插入html
rowhtml = '<tr><th>%s<td><input type="text" name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyHtml = replyHtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
    new = adict.copy()                          #值可能包含&、>等字符
    for field in fieldnames:                    #作为代码显示：被引号引起
        value = new[field]                      #转义html字符
        new[field] = cgi.escape(repr(value))
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__         #使用属性字典
        fields['key'] = key              #填充相应字符串
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields

def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            from person import Person
            record = Person(name='?', age='?')
        for field in fieldname:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields

db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action =='Fetch':
    fields = fetchRecord(db, form)
elif action =='Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyHtml % htmlize(fields))