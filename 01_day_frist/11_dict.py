#coding=UTF-8
d={'name':'chenlong','age':'18'}

print(d['name'])

#判断  键名是否存在
print('name' in d)

#get 获得知道键名的值

print(d.get('name'))

#pop 删除元素
d.pop('name')

print(d)

#dict是用空间来换取时间的一种方法