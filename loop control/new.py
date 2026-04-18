# # break
# # continue
# # pass

# for i in range(10):
#     if(i == 6):
#         pass

#     print(i)

# if(9 == 9):
#     pass


# nested loops

# for i in range(4): #outer
#     for k in range(2):
#         print(k)

#0
#   0
#   1

#1
#   0
#   1

#2
#3

#---------------------

n = 5

#10, 15
start = 10
end = 13

for i in range(start, end + 1): #1, 10 -> 1, 2, 3
    for j in range(1, 11): # 1 2 3 4...
        print(i * j)
    print("------------------")

#10
#   1 -> 10 * 1 = 10
#   2 -> 10 * 2 = 20
#   3 -> 10 * 3 = 30
#   4 -> ....
#   10 -> 10 * 10 = 100

#11
#12
#13