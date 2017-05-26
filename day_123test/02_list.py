#list是有序列表的集合

class_ =['1','2','3']



#length 获取元素的个数
length=len(class_)

#获取最后一个元素
class_[-1]

# 在 列表的最后一位上追加
class_.append('1')

# 插入指定的位置 insert(索引位置,要加入的值)
class_.insert(1,'join')

#删除末尾的元素 pop()
class_.pop()

#删除指定的元素 pop(索引的位置)
class_.pop(1)

print(class_)
print(length)