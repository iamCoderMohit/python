# accumulator
# search

# give me the sum of first 5 natural numbers

n = 5 # first 5 natural numbers

sum = 0 # accumulator

# for i in range(1, n + 1):
#     sum = sum + i #1 + 2 + 3 + 4 + 5

# print("sum =", sum)

# sum = 0

# 1
# sum = 1

# 2
# sum = 1 + 2 = 3

# 3
# sum = 3 + 3 = 6

# 4
# sum = 6 + 4 = 10

# 5
# sum = 10 + 5 = 15

# search

string = "SOMERANDOMSTRING"

# name = "mahima"
# 6
# 5

char = 'Z' # 11
isFound = False
ind = -1

print(string.find('Z'))

# print(string[11])
# print(string[12] == char)

# print(len(string))

# find the index of char in string

for i in range(len(string)): #0, 15
    if(string[i] == char):
        isFound = True
        ind = i

if(isFound == True):
    print("found at index", ind)
else:
    print("not found")

#S
#0
#M
#E

sum = 0

for i in range(1, 6):
    sum = sum + i

print(sum)