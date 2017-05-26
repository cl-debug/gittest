#coding=UTF-8
from _ast import Num

#默认参数

def add_end(L=[]):
    if L == []:
        L=[]
    L.append('end')
    print( L)

add_end()
add_end()
add_end()
add_end()



#可变参数
def add_change(*number):
    sum=0
    for i in number:
        sum=sum+i
    print( sum)
add_change(1,2,3,4,5,67,8)    

lists=[1,2,3,4,5,6,7]
#所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
add_change(*lists)

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例
def person(name,age,**kw):
    print 'name',name,'age','age','other',kw

person('bob', 18,city='chengdu')
#也可以传入任意个数的关键字参数
person('bob', 18,city='chengdu',agee='20')



#参数组合
def func(a,b,c=0,*arg,**kw):
    print 'a:',a,'b:',b,'c:',c,'args=',arg,'kw:',kw
    
func(1,2)    
func(1,2,3)
func(1,2,3,'a','b','c')
func(1,2,3,'a','b','c',kw='11')

#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。



