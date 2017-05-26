#coding=UTF-8

#获取对象类型

print type(11)

import types

str=type('abs')

print(str==types.StringType)

unicde1=type(u'abc')

print(unicde1==types.UnicodeType)

print(type([])==types.ListType)

#所有类型本身的类型就是TypeType

type(int)==type(str)==types.TypeType


#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

isinstance(object, class_or_type_or_tuple)


#能用type()判断的基本类型也可以用isinstance()判断：

isinstance('a', str)

isinstance(u'a', unicode)