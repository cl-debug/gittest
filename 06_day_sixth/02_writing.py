#coding=UTF-8
#传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f= open('read.txt','w')

f.write('chenlong22222')
f.close()

#当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，
#操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了

with open('read.txt','w') as f:
    f.write('Hello')

