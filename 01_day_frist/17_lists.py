#coding=UTF-8

a=[x for x in list(range(10)) if x%2==0]

#两层循环
b=[x+y for x in 'ABCDEF' for y in 'GHIKL']
print(a)
print(b)

#列出当前目录下所有的文件 os

import os

d=[d for d  in os.listdir('.')]
print(d)

