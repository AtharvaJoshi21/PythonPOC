#!/usr/bin/python

def initWrapper(func):
    def Init():
        data=func()
        next(data)
        return data
    return Init

@initWrapper
def Increement():
    x=yield
    yield x+10
 
data=Increement()
print(data.send(10))
