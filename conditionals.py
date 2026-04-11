# conditionals

# if else

# if(1 > 6):
#     print("greater")
# else:
#     print("not greater")

# age = int(input("Enter your age : "))

# if(age >= 18):
#     print("eligible")
# elif(age <= 0):
#     print("age can't be less than 0, idiot")
# elif(age > 100):
#     print("age cant be greater than 100")
# else:
#     print("not eligible")

phy = float(input("Enter you marks in physics : "))
che = float(input("Enter you marks in chemistry : "))
mat = float(input("Enter you marks in maths : "))

# (phy + che + mat) / 300 * 100

percentage = ((phy + che + mat) / 300) * 100

# 90 - A
# 70 - B
# 50 - C
#    - D

if(percentage >= 90 and percentage <= 100):
    print(f"{percentage}% A")
elif(percentage >= 70 and percentage < 90):
    print(f"{percentage}% B")
elif(percentage >= 50 and percentage < 70):
    print(f"{percentage}% C")
else:
    print(f"{percentage}%D")