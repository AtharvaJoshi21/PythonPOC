# WAP to implement operator overloaded slicing logic on list.

class ListWrapper:
    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8]
    
    def __getitem__(self, obj):
        print(obj.start)
        print(obj.stop)
        print(obj.step)
        return self.list[obj.start:obj.stop:obj.step]

def main():
    lst = ListWrapper()
    print(lst[1:7:2])

if __name__ == "__main__":
    main()