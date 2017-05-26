#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）

d= {"a":"1","b":"2"}

#默认情况下，dict迭代的是key
for i in d:
	print(i)

#迭代value，可以用for value in d.values()
for i in d.values():
	print(i)

#如果要同时迭代key和value，可以用for k, v in d.items()

for i in d.items():
	print(i)	

#判断一个是否是可迭代对象
#collections模块的Iterable类型判断

from collections import Iterable

print(isinstance('abc',Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身

for i in enumerate(["A","B","C"]):
	print(i)