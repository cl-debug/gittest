#coding=UTF-8
#函数作为返回值
def  lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f1=lazy_sum(1,2,3,4,5,6)

f2=lazy_sum(1,2,3,4,5,6)

#f不是返回的结果 而是一个求和的结果函数

# 直接执行函数才可以执行
print(f1())    

print(f1==f2)

#闭包内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包(Closure)