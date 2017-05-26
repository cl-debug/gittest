import types

a=type(123)
b=type(abs)
print(a)
print(b)

#type(123)==types.TypeType


c=isinstance(11,int)
print(c)

#获得一个对象的属性和方法
dir()
print(dir("ABC"))