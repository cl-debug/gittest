#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
d={"chen":1,"long":2,"ni":3}

for i in d:
	print(i)
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values() 注意是values 不是 value

for x in d.values():
	print(x)

# 同时迭代 key 和 value   for k,v in d.items()

for k,v in d.items():
	print(k)
	print(v)	

# 字符串也可迭代

#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。



# d=list(range(20))

for x,y in d.items():
	print(x)
	print(y)
