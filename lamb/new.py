a = [1, 2, 3, 4, 5]

# [1, 4, 9, 16, 25]

def square(n):
    return n ** 2

# i = 0

# while i < len(a):
#     print(square(a[i]))
#     i += 1

# b = map(lambda x: x ** 2, a)

b = map(square, a)

print(list(b))

# d = 1.2

# print(int(d))


fruits = ["banana", "mango", "pineapple"]

# print(fruits[1].upper())

ans = map(lambda x: x.upper(), fruits)

# print(list(ans))

e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(n):
    if(n % 2 == 0):
        return True
    else: 
        return False
    
b = filter(lambda x: x % 2 == 0, e)

print(list(b))