name = input("Please enter a string: ")
replaceToken = input("Please enter token to replace: ")
print (name)

name2 = name[0] + name[1:].replace(name[0], replaceToken)
print (name2)