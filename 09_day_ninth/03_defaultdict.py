#coding=UTF-8

#defaultdict


#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import  defaultdict

#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
da=defaultdict(lambda:"11")

print da

da["key1"]="key1"

print da

print da["key2"]