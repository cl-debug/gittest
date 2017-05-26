#参数组合
#python 定义参数时 可用 必选参数 默认参数 可变参数 关键字参数 和命名关键字参数
#定义的顺序必须是 必选参数 默认参数 命名关键字参数和关键字参数
# * 表示可变参数,接收的是一个tuple ** 表示关键字参数 接收的是dict

def func1(a,b,c=0,*arg,**kw):
    print("a:",a,"b:",b,"c:",c,"arg:",arg,"kw:",kw)


# * 表示命名关键字参数，变量名称必须和参数名称相同， 参数前的 ** 表示接收的是dict
def func2(a,b,c=0,*,d,**kw):
    print("a:",a,"b:",b,"c:",c,"d:",d,"kw:",kw)

func1(1,2)

func1(1,2,3)

#  "a","b" 表示可变参数
func1(1,2,3,'a','b')

func1(1,2,3,'a','b','c')

# x= 'nihao'
func1(1,2,3,"a",x="nihao")

func2(1,2,d='11',ext='nihao')

args=(1,2,3)
kw={'chenlong':'chenlong','age':18}

func1(*args,**kw)

func2(*args,**kw)

#*args是可变参数，args接收的是一个tuple；  **kw是关键字参数，kw接收的是一个dict。

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。