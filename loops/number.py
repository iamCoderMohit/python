# number guessing game

# a = 10 (computer generated number)
# enter your guess : 10, 20, 30
# ask the user till he gets the correct number
# 1 - 100
# 45
# 30 - this number is less than the computer number
# only 5 attempts are allowed

# loop (bar bar puchna hai user se)
# conditionals (if, else)
# input()
# break

a = 10 # random number
attempts = 0

print("Number guessing game")
print("Rules - random number is b/w 1 - 100, you have 5 attempts")

print("---------------------------------")

while True:
    userInp = int(input("Enter your guess : "))
    attempts = attempts + 1

    if(attempts == 5):
        print("you have exhausted the total attempts")
        break

    if(userInp < a):
        print("this number is lesser than the random number")
    elif(userInp > a):
        print("this number is greater than the random number")
    else:
        print(f"you have guessed it right and you took {attempts} attempts")
        break