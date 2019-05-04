#!/usr/bin/python

def initWrapper(func):
    def Init():
        data=func()
        next(data)
        return data
    return Init

def Increement():
    x=yield
    yield x+10
    
init = initWrapper(Increement)
data=init()
print(data.send(10))
