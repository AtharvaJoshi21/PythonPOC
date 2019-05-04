#!/usr/bin/python
def init(Data):
    next(Data)
def increament():
    x= yield
    yield x+10

data = increament()
init(data)
#next(data)
#data.send(None)
print(data.send(10))
