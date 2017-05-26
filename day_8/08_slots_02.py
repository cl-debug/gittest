#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student(object):
	__slots__=('name','age') # 用tuple定义允许绑定的属性名称

# 只允许设置name 和age 属性
#__slots__