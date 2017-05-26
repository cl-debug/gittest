#coding=UTF-8

import json

class Student(object):
    def __init__(self,name,age,sorce):
        self.name=name
        self.age=age
        self.sorce=sorce
s=Student('chenlong',20,18)

json.dumps(s)        