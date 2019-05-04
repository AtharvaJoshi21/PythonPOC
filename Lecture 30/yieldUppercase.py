#write a function which accepts string via yield and returns upper case

#!/usr/bin/python

def initWrapper(func):
    def Init():
        data=func()
        next(data)
        return data
    return Init

@initWrapper
def toUpper():
    x=yield
    yield x.upper()
 
data=toUpper()
print(data.send('swapnil'))

