#write class with name as autogenerate with init method in it.
class AutoGenerate:
    def __init__(self,start,end,step=1):
        self.start=start
        self.end = end
        self.step = step
    def next(self):
            self.start+=self.step
            if self.start >=self.end:
                raise StopIteration
            return self.start
    def __next__(self):
        yield self.next()
    def __iter__(self):
        return self

def main():
    x= AutoGenerate(0,100,5)
    for y in x:
        print y
if __name__=="__main__":
    main()
