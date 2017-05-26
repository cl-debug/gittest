#coding=UTF-8
#\ 符号表示转义
print('I\'m \"OK\"')
print 'T\'m \"Ok"'



#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('name\nchenlong')
print('name\tchenlong')
print('\\')
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义

print(r'name\nchenlong')

#Python允许用'''...'''的格式表示多行内容

print('''name
chen
long''')

print 10.0 / 3