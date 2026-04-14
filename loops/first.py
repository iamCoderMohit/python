# # DRY - don't repeat yourself

# # while, for

# i = 1

# while i < 10: # when i is 10
#     print(i) # 1 2 3 4 5 6 7 8 9 
#     i = i + 1 # 2 3 4 ...... 10

# print('hey there')

# # while condition:
# #   content (things to be repeated)
# #   updation

# print hello world 10 times
 

# while i < 11:
#     print(i, "hello world")
#     i = i + 1 # updation

# while True:
#     print("yeyyyyy")

i = 1 # counter varible
# don't print 3

# Continue - skips work for current iteration

# while i < 10:
#     if(i == 3): #
#         i = i + 1
#         continue

#     print(i)
#     i = i + 1
# a = 100
# while a <= 1000:
#     if(a == 500):
#         a = a + 100
#         continue

#     print(a)
#     a = a + 

# Break - break the loop at a specific condition

i = 0
while i < 10:
    if(i == 5):
        break

    print(i)
    i = i + 1

print("loop is broke")