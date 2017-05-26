#coding=UTF-8

#try...except...finally...

#错误处理机制

try:
    print 'try'
    r=10/int('a')
    print 'result',r
except ValueError,e:
    print 'Value',e    
except ZeroDivisionError,e:
    print 'except', e
else: #没有发生错误时执行
    print "else"    
finally:
    print 'Finally'
print   'END'       

#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽

try:
    foo()
except StandardError,e:
    print 'StandardError'
except ValueError,e:
    print 'ValueError'   
#第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类，如果有，也被第一个except给捕获了
         
    
        