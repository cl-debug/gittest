#coding=UTF-8

#操作文件或者目录

import os

#获取当前文件的绝对路劲
print os.path.abspath('.')

#创建某个目录
os.mkdir('D:/wamp/wamp/www/python/my_test/06_day_sixth/chen.txt')
#删除某个目录
os.rmdir('D:/wamp/wamp/www/python/my_test/06_day_sixth/chen.txt')

#合并两个路劲
print os.path.join("D:/wamp/wamp/www/python/","my_test/06_day_sixth")

#拆分路劲 后一部分总是最后级别的目录或文件名
print os.path.split(os.path.abspath('.'))

#获取文件扩展名
print os.path.splitext('/path/to/file.txt')

#文件重命名
#os.rename('read.txt', 'my.txt')
#删除文件
#os.remove('read.txt')




#复制文件
#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

#列出当前目录下的所有目录，只需要一行代码
print  [x for x in os.listdir('.') if os.path.isfile(x)]

#列出所有的py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



