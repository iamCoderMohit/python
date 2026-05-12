# word: meaning

# key: value

d = {
    "name": "mahima",
    "course": "python",
    "city": "up",
    1: 10,
    False: True,
    "subj": ["math", "phy", "chem"]
}

# print(d[False])


d["name"] = "mohit"

d["marks"] = 100
# print(len(d))

m = d["subj"]

# print(d["subj"][1])

# print(m[0])

d.pop("name")

# d.clear()

del d["city"]

print(d)