#coding=UTF-8

#re 模块

# 匹配规则上加r前缀 不考虑转义问题

import re



print re.match(r"^\d{3}\-\d{3,8}$", '010-12345')


print re.match(r"^\d{3}\-\d{3-8}$", "010 12346")

#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None