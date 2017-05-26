#coding=UTF-8


import sys


def test():
    #导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
    args=sys.argv
    if len(args)==1:
        print 'hello'
    if len(args)==2:
        print 'helle %s!'% args[1]
    else:
        print'too many'
        
        
            