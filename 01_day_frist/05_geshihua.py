#coding=UTF-8
name="陈龙"
age=12
#在Python中，采用的格式化方式和C语言是一致的，用%实现
result='Hello,%s,you has $%s' %(age,age)

print(result)

#%运算符就是用来格式化字符串的

#在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

#常用占位符
    #%d 整数
    #%s 字符串
    #%f 浮点数
    #$x 16进制
    
#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

info="I have %d%%"%(40)

print(info)