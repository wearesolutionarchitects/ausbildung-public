from multipledispatch import dispatch

@dispatch(int,str)
def func(x,c):
    print("Integer1" + c)
    return x * 2

@dispatch(float)
def func(x):
    print("Float")
    return x / 2

@dispatch(str) # Dekorator
def func(x):
    print("String")
    return ("Einen String")

# Driver code
print(func(2.0))

func(2,"joj")

1 + 2
"öölk" + "ölkölk"

#func("Hallo")