#coding=UTF-8

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法


print(dir('abc'))

print(len('abc'))

print('abc'.__len__())


#getattr()、setattr()以及hasattr()
    
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x        
    
obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
True
# obj.x
9
print hasattr(obj, 'y') # 有属性'y'吗？

False
setattr(obj, 'y', 19) # 设置一个属性'y'

print hasattr(obj, 'y') # 有属性'y'吗？
True
print getattr(obj, 'y') # 获取属性'y'
19
#obj.y # 获取属性'y'
19