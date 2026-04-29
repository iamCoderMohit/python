x = 4 # global variable
b = 7

def info():
    c = 9 # local variable
    global x
    global b
    x = 10

info()

# print(x)

course = "cpp"

def func1():
    name = "mahima" # local

    def func2():
        nonlocal name
        global course

        course = "python"
        name = "not mahima"

    func2()

    print(name, course)

func1()

y = 9
def demo():
    print(y)

    z = 10

# demo()
# print(z)