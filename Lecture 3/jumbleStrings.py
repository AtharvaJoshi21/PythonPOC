#WAP to accept a string from user and jumble the string such as:
#1. print odd indexed characters suffixed by even indexed characters
#2. print odd indexed characters suffixed by even indexed characters with reversed strings

name = input("Please enter a string: ")
print ("Jumbled string is :")
name1 = name[0::2] + name[1::2]
print(name1)

name2 = name[::-2] + name[-2::-2]
print(name2)