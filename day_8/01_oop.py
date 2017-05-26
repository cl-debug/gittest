##class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的	
class Student(object):
	pass

#创建实例是通过类名+()
bar = Student()

print(bar)	

bar.name="chenlong"
#给实例bart绑定一个name属性
print(bar.name)