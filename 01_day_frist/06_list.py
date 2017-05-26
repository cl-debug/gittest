#coding=UTF-8
from sys import callstats
calssmates=['CHEN','LONG']

print calssmates

#len 函数获得list元素个数
print(len(calssmates))

#索引访问list的元素 从0开始 负数则是倒去

print(calssmates[1])

#insert 插入指定位置

calssmates.insert(2, "cool")

print(calssmates)

#pop 删除，末尾的元素 删除指定的元素pop(索引)

calssmates.pop()
print(calssmates)

calssmates.pop(0)

print(calssmates)