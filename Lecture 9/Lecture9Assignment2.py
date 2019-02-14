#Variable arguments dictionary (Key-Value Pair)

def VariableArgsDictionary(a, b, *args, **kwargs):
    print (a,b)
    print(type(args), type(kwargs))
    for x in args:
        print(x)
    for y in kwargs:
        print(y, kwargs[y])
    
def main():
    VariableArgsDictionary(10,20,1,2,3,4,5,6,7,name="Atharva", hobby="Music")

if __name__ == "__main__":
    main()