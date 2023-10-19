#strings are immutable if we want to update and add sub string need convert into list beacuse list are mutable in nature
string1 = "hello"
print(string1)
string2 = 'world'
print(string2)
string3 = ''' string program given the input'''
print(string3)
string4 = "abdr"
print(string4)
list = list(string4)
print(list)
list[3] = "sh"
print(list)
# update entire string using exist string also
string1 = "hello world"
print(string1)
