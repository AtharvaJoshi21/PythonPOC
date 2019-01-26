name = input("Please enter a string: ")
print ("Jumbled string is :")
name1 = name[0::2] + name[1::2]
print(name1)

name2 = name[::-2] + name[-2::-2]
print(name2)