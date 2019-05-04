#write a function which accepts time and print log with time structure

#!/usr/bin/python
import time
def LogDecorator(func):
    def log(args):
        return func(str(time.time())+" "+args)
    return log

def NameDecorator(func):
    def log(args):
        return func("Swapnil Shinde:"+args)
    return log

@LogDecorator
@NameDecorator
def Logger(data):
    print("Logged {}",format(data))

def main():
    Logger("Top")
    time.sleep(1)
    Logger("PS")

if __name__=='__main__':
    main()
