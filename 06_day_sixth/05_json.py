#coding=UTF-8

import json

#我们先看看如何把Python对象变成一个JSON
d=dict(name='chenlong',age=20)
print json.dumps(d)

#把JSON反序列化为Python对象
json_str='{"name":"chenlong","age":88}'
print  json.loads(json_str)
#有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str