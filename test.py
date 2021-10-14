var = 1
def nameOfThefuncion(arg1="default1", arg2):
    print("Hello!!!!")
    print(arg1)
    print(arg2)
    global var
    var=2


print(var)
nameOfThefuncion()
print(var)