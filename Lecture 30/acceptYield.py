#!/usr/bin/python
def increament():
    x= yield
    yield x+10

data = increament()
next(data)
#data.send(None)
print(data.send(10))
