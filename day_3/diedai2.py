#如何判断一个对象是可迭代对象呢
#方法是通过collections模块的Iterable类型判断：

from collections import Iterable

#isinstance 表示是否在范围中
result = isinstance('abc',Iterable)
result = isinstance(["1",2],Iterable)
result = isinstance(1234,Iterable) # 整数不可迭代
print(result)



#Python内置的enumerate函数可以把一个list变成索引-元素对 类似于foreach($value as $k=>$v)

list_= [1,2,3,4,5,6,7,8,9]

for  x in enumerate(list_):  
	print(x[1])
	
#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。	