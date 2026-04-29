

def func1():
    x = 1

    def func2():
        nonlocal x

        x = 10
        print(x)

    func2()

func1()