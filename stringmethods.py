# strings are immutable
string1 = "hello"
string2 = "Abdr\n"
# it creates new copy for existing string
print(string1 . upper())
print(string2 . lower())
string3 = "quality $$$$$"
# it remove leading and trailing whitespaces and  speical characters
print(string3 . rstrip("$"))
string4 = "!!! quality $$$$"
print(string3 . rstrip("!"))
print(string1 . replace("hello", "sham"))
print(string3 . split("$"))
string5 = "introduction to strings"
print(string5)
print(string5.capitalize())
length = (len(string5))
print("length of string5 = ",length)
print(string5.center(50))
count1 = (string4.count("$"))
print("count # in string4 = ", count1)
#check $ is present or not
print(string4.endswith("$"))
print(string4.endswith("to", 4, 20))
print(string5.endswith("to"))
# if not exist return the -1
find = (string5.find("to"))
print("find = ", find)
print(string1.find("to"))
# checking only a-z,A-Z,0-9 present in string ,if present given true otherwise false
isalnum = (string4.isalnum())
print("isalnum = ", isalnum)
#check only a-z and A-Z present in string , if present given true oterwise false
isalpha = (string1.isalpha())
print("isalpha = ", isalpha)
islower = string2.islower()
print("islower = ", islower)
isprintable = string2.isprintable()
print("isprintable = ", isprintable)
# using spacebar and tab given space then return true
isspace = string5.isspace()
print("isspace = ", isspace)
startswith = string1.startswith("ab")
print("startswith = ", startswith)
swapcase = string2.swapcase()
print("swapcase = ", swapcase)
#print string as title
title = string5.title()
print("title = ", title)
#check each index value if given substring is present or not
print(string1.index("to"))
