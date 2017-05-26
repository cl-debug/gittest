#coding=UTF-8 
#切分字符串
import re
r= 'a b c   d'
#无法识别连续的空格
print r.split(' ')
#正则匹配
print re.split(r'[\s\,]+',r)


