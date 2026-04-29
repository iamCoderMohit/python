from math import pi

x = 10

def info():
    # x = 30 #local

    def info2():
        print(pi)

    info2()

info()

# LEGB = LOCAL, ENCLOSED, GLOBAL, BUILT-IN

