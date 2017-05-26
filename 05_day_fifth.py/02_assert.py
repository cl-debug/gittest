#coding=UTF-8


#凡是用print来辅助查看的地方，都可以用断言（assert）来替代

def foo(s):
    n=int(s)
    assert n!=0 ,'n is zoo'
    return 10/n

foo('0')