#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

import functools

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
print(int('123456'))

print(int('111111',base=2))

init1=functools.partial(int,base=2)

print(init1('100'))

#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。