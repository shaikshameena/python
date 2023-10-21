# *args for variable number of arguments
def myfun(*argv) :
    for arg in argv :
        print(arg)
myfun("iam", "shameena ", "working in qualizeal")

# *kwargs for variable number of keyword arguments
def myfun(**kwargs) :
    for key, value in kwargs.items():
        print("%s = %s " %(key, value))
myfun(first = "i am ", mid = "shameena", last = "working in qualizeal")
