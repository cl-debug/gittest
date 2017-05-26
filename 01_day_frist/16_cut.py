#coding=UTF-8

l=[1,2,3,4,5,6,7,8,9]

print(l[0:3:2])
#所有的书 每2个去一个
print(l[::2])

#原样复制
print(l[:])

#tuple也可以用切片操作，只是操作的结果仍是tuple
tuple=(1,2,3,4,5,6)
print(tuple[2:5])

#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
str='ASDFGHJKL'
print(str[1:6:2])