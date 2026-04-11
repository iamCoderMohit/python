# # nested conditionals

# # 18+
# # indian citizen
# # mohit and mahima

# age = 19
# citizen = "usa" #usa canada
# name = "raj"

# if(age >= 18 and age > 0 and age < 100):
#     if(citizen == "india"):
#         if(name != "mahima" and name != "mohit"):
#             print("you can vote")
#         else:
#             if(name == "mohit"):
#                 print("name is mohit and he is terrorist")
#             else:
#                 print("name is mahima and she is terrorist too")
#     else:
#         print("you are not inidan citizen")
# else:
#     print("age is not valid or less than 18")

# #one linear expression / ternary

# # check if the name is mahima or not
# name = "sdgf"
# num = 6
# a = 7 + 7 if num == 6 else 7 - 7

# print(a)

# # print("name is mahima" if name == "mahima" else "no she's not mahima")

# # karna kya hai if condition else work

# match case

# APPROVED CANCEL REFUND

txn = "JSJDFHJ"

match txn:
    case "APPROVED":
        print("txn is approved")
    case "CANCEL":
        print("txn is cancelled")
    case "REFUND":
        print("money is refunded")
    case _:
        print("undefined case")

print("yes" if 5 > 6 and 8 > 0 else "no")