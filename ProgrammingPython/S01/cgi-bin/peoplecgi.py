"""
实现用来查看和更新保存在shelve中类实例的基于Web的界面；
shelve保存在服务器上（如果是本地机器的话就是同一个服务器）
"""
import cgi, shelve, sys, os                      #cgi.test()转储输入
shelvename = 'class-shelve'                     #shelve文件在当前工作目录
fieldname = ('name', 'age', 'job', 'pay')
form = cgi.FieldStorage()                        #解析表单数据
print('Content-type: text/html')              #响应html中的hdr和空行
sys.path.insert(0, os.getcwd())                 #为了this和pickler查找person

#主html模板
