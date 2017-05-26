#关键字参数
def pe(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

pe('chenlong',18,city='chengdu')

pe('chenlong',18)

kw={'name1':'chenlong'}

#  **kw 表示把kw这个dict的所有key-vale 用关键字参数传入到函数的**kw ，kw获得的是一个dict  注意kw获得的dict是 参数kw的一份拷贝，对kw的改动不会影响到函数外的kw。
pe("chenlong",18,**kw)