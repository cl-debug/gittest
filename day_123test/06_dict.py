#使用键-值（key-value）存储 类似于关联数组
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
# 取得数据
print(d['Michael'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入

d['Adam'] = 67

print(d)

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

'Thomas' in d

#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)



#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

d.pop('Bob')

#这个通过key计算位置的算法称为哈希算法（Hash）。