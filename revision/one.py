# tuple - unchangeable
# dictionaries - key value pairs
# sets - no repetition, unordered

a = (12.34343, 13.232323)

# a[1] = 34.23232

# print(a[1])

b = {1, 1, 1, 2, 3, 4, 5}
c = list(b)

# print(c[3])

d = {
    "name": "mahima",
    "course": "python",
    "marks": [23, 45, 56, 67]
}

# d["course"] = "cpp"
# d["age"] = 90

m = d["marks"]
# print(d["marks"][3])

print(m[3])