a = ["rohit", "ram", "mohit", "mahima", "rohit"]

# 56

# print(a)

# a.append("rahul")
# a.clear()
# newList = a.copy()

# print(newList)

# print(a.count("aksdgfhasd"))

a.remove("mohit")

# print(a)

# list slicing

classStudents = [10, 20, 56, 34, 23, 89]

# class 1 -> 10, 20

class_one = classStudents[0:2]

# print(classStudents)
# print(class_one)

class_two = classStudents[2:4]

# print(class_two)

demo = classStudents[:4]

# print(demo)

# sort

# ASCENDING, DESCENDING


# randomList.sort(reverse=True)

# print(randomList)

# newList = sorted(randomList, reverse=True)

# print(newList)

def sortCustom(l):
    biggestItem = l[0]

    for i in l: #23, 12, 67...
        if(i > biggestItem):
            biggestItem = i

    return biggestItem
        

randomList = [23, 12, 67, 89, 0, 34]

ans = sortCustom(randomList)

print(ans)