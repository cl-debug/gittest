#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name,age,**kw):
    if 'city' in kw:
    #有city参数
        pass
    if 'job' in kw:
    #有job参数
        pass
    print("name:",name,"age:",age,"other:",kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)



#限制关键字参数名，用命名关键字参数，如只接收city 和 job作为关键字参数，必须加* 作为特殊分隔符，否则无用
def person_key(name,age,*,city,job):
    print(name,age,city,job)

person_key('chenlong',18,city="chengdu",job="php")



#  关键字参数可以加默认值
def person_key_default(name,age,*,city="chengdu",job):
    print(name,age,city,job)

person_key_default('cl',18,job='php')
