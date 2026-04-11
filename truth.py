# truthy and falsy values

a = 0 #falsy

# -1, 1 -> truthy

# print(bool("dsfh"))

a = 1 < 2 < 3

# (1 < 2) and (2 < 3)

# print(a)

b = 7 == 7 <= 90 > 89

# (7 == 7) and (7 <= 90) and (90 > 89)

b = 8 >= 8 != 90

# print(b)

#short circuit evaluation

c = 5 != 5 < 90 == 90 > 10

# (5 != 5) and (5 < 90)

print(c)